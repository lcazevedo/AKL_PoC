"""Recompute the proof-of-concept numbers reported in the paper from the files of this repository.

Run from the repository root:  python verify_poc_numbers.py
Requires: pandas, pyarrow, numpy, scikit-learn.
"""
from pathlib import Path

import numpy as np
import pandas as pd
from sklearn.metrics import roc_auc_score

R = Path("results")
THRESHOLDS = {"challenges": 0.2, "directions": 0.5}


def wilson(k, n, z=1.959964):
    p = k / n
    d = 1 + z * z / n
    c = (p + z * z / (2 * n)) / d
    h = z * np.sqrt(p * (1 - p) / n + z * z / (4 * n * n)) / d
    return c - h, c + h


def fmt(k, n):
    lo, hi = wilson(k, n)
    return f"{k} of {n} ({k / n:.2f}, 95% Wilson {lo:.2f}-{hi:.2f})"


def norm(s):
    return s.astype(str).str.strip().str.lower()


print("== Steps 1 and 2: retrieved records")
raw = pd.read_csv(R / "step1/step1_retrieved_records.csv", keep_default_na=False, dtype=str)
print("retrieved:", len(raw), raw["source"].value_counts().to_dict())
fate = raw["fate"].value_counts()
dedup = len(raw) - fate["removed_step1_duplicate"]
print("after deduplication:", dedup, "| after cleaning:", dedup - fate["removed_step2_cleaning"])

print("\n== Step 4: expert relevance labels")
lab = pd.read_csv(R / "step4/step4_expert_relevance_labels.csv")
lab["doi"] = norm(lab["doi"])
print("labels:", len(lab), lab["label"].value_counts().to_dict())
exp = pd.read_csv(R / "step4/step4_active_expansion_rounds.csv")
r1, r2 = set(exp.loc[exp["round"] == 1, "doi"]), set(exp.loc[exp["round"] == 2, "doi"])
no = lab["label"] == "no"
agree = norm(exp["expert_label"]) == norm(exp["llm_suggestion"])
print(f"expansion candidates: {len(exp)} | expert agreed with the LLM suggestion: {int(agree.sum())} ({agree.mean():.0%})")
print("not-relevant labels: initial", int((no & ~lab.doi.isin(r1 | r2)).sum()),
      "| after round 1", int((no & ~lab.doi.isin(r2)).sum()), "| after round 2", int(no.sum()))

print("\n== Step 5: relevance filter")
p5 = pd.read_csv(R / "step5/step5_relevance_predictions.csv")
print("cleaned documents:", len(p5), "| retained:", int((p5["predicted_relevance"] == "yes").sum()))
band = p5["proba_yes"].between(0.40, 0.60)
print(f"uncertainty band 0.40-0.60: {int(band.sum())} ({band.mean():.1%})")

print("\n== Step 6: topic assignments")
t6 = pd.read_parquet(R / "step6/topic_assignments_layer3.parquet")
print("documents:", len(t6), "| topics:", t6["topic"].nunique(), "| unassigned:", int((t6["topic"] == -1).sum()))

print("\n== Step 7: extraction")
f7 = pd.read_parquet(R / "step7/step7_extractions_final.parquet", columns=["vector", "scope"])
print("final rows:", len(f7), f7["scope"].value_counts().to_dict())
print(f7["vector"].value_counts().to_string())
vs = pd.read_parquet(R / "step7/step7_verifier_scores.parquet")
for v, thr in THRESHOLDS.items():
    before = pd.read_parquet(R / f"step7/step7_{v}_before_verifier.parquet", columns=["doi", "text_sha1"])
    print(f"verifier {v}: {len(before)} rows before, {int((f7['vector'] == v).sum())} after "
          f"({(f7['vector'] == v).sum() / len(before):.1%}), threshold {thr}")

print("\n== Step 8: extraction audits")
for v, thr in THRESHOLDS.items():
    a = pd.read_csv(R / f"audits/step8_audit_{v}.csv", keep_default_na=False)
    a["correct"] = norm(a["audit_label"]) == norm(a["micro_label"])
    a["states_vector"] = norm(a["audit_label"]) != "none"
    s = vs[vs["vector"] == v].drop_duplicates("text_sha1")[["text_sha1", "p_yes"]]
    a = a.merge(s, on="text_sha1", how="left")
    kept = a[a["p_yes"] >= thr]
    print(f"{v}: label accepted {fmt(int(a.correct.sum()), len(a))}")
    print(f"  sentence states the vector: {int(a.states_vector.sum())} of {len(a)} ({a.states_vector.mean():.2f})")
    print(f"  after verifier: label accepted {fmt(int(kept.correct.sum()), len(kept))}, "
          f"states the vector {int(kept.states_vector.sum())} of {len(kept)} ({kept.states_vector.mean():.2f})")
    tv = a[a.states_vector]
    print(f"  conditional recall of the verifier (sentences that state the vector and are kept): "
          f"{int((tv.p_yes >= thr).sum())} of {len(tv)} ({(tv.p_yes >= thr).mean():.2f})")
    print(f"  verifier AUC (target: sentence states the vector): {roc_auc_score(a.states_vector, a.p_yes):.2f}")
