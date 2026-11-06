# AKL proof of concept: machine learning in chemistry and materials science

This repository contains the code, configuration, results, and audit artifacts of the proof of concept of the orchestrated implementation of Automated Knowledge Landscapes (AKL), reported in:

> Azevedo, L. C.; Prati, R. C. *Automated Knowledge Landscapes: A Human-in-the-Loop Semantic Bibliometric Roadmap for Strategic Discovery.* [TODO: journal, year, DOI]

The proof of concept applied the nine-step pipeline to a corpus on machine learning in chemistry and materials science (2000-2026, drug discovery and biological QSAR excluded). Its purpose was to verify the automation at the scale of a research domain. The topics and extractions in this repository illustrate the output of the pipeline and are not presented as findings.

| Stage | Count |
|---|---|
| Records retrieved (Web of Science 52,035 + OpenAlex 19,730) | 71,765 |
| After deduplication | 61,403 |
| After cleaning (Step 2) | 58,000 |
| After the relevance filter (Step 5) | 48,030 |
| Topics in the selected layer (Step 6) | 60 |
| Extraction rows after verification (Step 7, 12 vectors) | 426,238 |

## Code

The folder `code/` contains the workers, agent instructions (`AGENTS.md`, `.opencode/skills/`), run scripts, and requirements used in the proof of concept. It is identical to the release [TODO: tag] (commit [TODO: hash]) of [AKL_Pipeline_Automation](https://github.com/lcazevedo/AKL_Pipeline_Automation), which is the repository to use for new projects.

## Repository layout

| Path | Content |
|---|---|
| `config/project_config.md` | Research question, data sources and queries, relevance criteria, extraction vectors, and Step 8 questions |
| `config/pipeline_config.yaml` | Technical parameters of the execution (models, servers, seeds, thresholds) |
| `config/pipeline_state.json` | Final state of the pipeline, with the notes of each step |
| `results/step1/step1_retrieved_records.csv` | The 71,765 retrieved records: source, identifier, DOI, year, document type, title (OpenAlex only), `title_sha1`, missing abstract, and fate in Steps 1 and 2 (removed as duplicate, removed in cleaning, or kept in the 58,000 cleaned documents) |
| `results/step4/step4_expert_relevance_labels.csv` | The 569 expert relevance labels used to train the filter (344 relevant, 225 not relevant) |
| `results/step4/step4_active_expansion_rounds.csv` | The two rounds of active expansion of the labels: candidate DOI, round, expert label, and the suggestion of the language model |
| `results/step5/step5_relevance_predictions.csv` | Prediction and P(relevant) of the SetFit filter for the 58,000 cleaned documents, with the source of each record |
| `results/step6/topic_assignments_layer3.parquet` | Topic of each of the 48,030 relevant documents in the selected layer (60 topics) |
| `results/step6/topics_layer3_summary.csv` | Size, name, and c-TF-IDF terms of each topic |
| `results/step6/step6_cvi_report.md`, `step6_kneedle_plot.png` | Validity indices of the six layers and the Kneedle analysis |
| `results/step6/step6_seed_test_output.txt` | Output of `code/tools/seed_test.py`: refit of EVoC with seed 42, compared with the saved layers, and with seeds 7 and 123 |
| `results/step7/step7_extractions_final.parquet` | Final extraction table (long format, one row per document, vector, and label) |
| `results/step7/step7_challenges_before_verifier.parquet`, `step7_directions_before_verifier.parquet` | Sentence-level challenge and direction rows before the sentence verifier |
| `results/step7/step7_verifier_scores.parquet` | Verifier score P(yes) of each challenge and direction sentence |
| `results/audits/step8_audit_challenges.*`, `step8_audit_directions.*` | Expert audits of the extraction (97 challenge and 95 direction sentences) |
| `reports/` | Reports of Steps 2, 5, 8, and 9 and the figures of Steps 8 and 9 |
| `docs/decision_log.md` | Analytic decisions taken during the execution |
| `verify_poc_numbers.py` | Recomputes the counts and audit metrics reported in the paper from the files above |

## Data conventions

- **DOI.** Lower case, without the `https://doi.org/` prefix.
- **Text of the records.** Titles, abstracts, and sentences of Web of Science records are not redistributed, following the Clarivate terms of use. In the Step 7 tables and in the audits, the column `original_text` is kept only for records whose source is OpenAlex and is empty for Web of Science records.
- **Text hash.** The columns `text_sha1` and `title_sha1` are the SHA-1 hash of the UTF-8 encoded text of the sentence, abstract, or title, after removing leading and trailing white space. Researchers with access to the Web of Science records can compute the same hash on their copy of the text to recover each row. The verifier scores are keyed by `vector`, `doi`, and `text_sha1`.
- **Audit metrics.** A label is counted as correct when the expert label (`audit_label`) equals the label of the model (`micro_label`), ignoring case. The value "None" is read as text, not as an empty cell.

## Verifying the reported numbers

```bash
pip install pandas pyarrow numpy scikit-learn
python verify_poc_numbers.py
```

The script prints the retrieval and cleaning counts of Steps 1 and 2, the label counts of Step 4, the filter counts and the uncertainty band of Step 5, the topic counts of Step 6, the rows per vector and the effect of the verifier in Step 7, and the accuracy of the extraction audits with Wilson intervals and the AUC of the verifier.

## Not included

- The records retrieved from the Web of Science (titles, abstracts, and author data), for the licensing reasons above. The queries are in `config/project_config.md`.
- Model weights. The models are public and are named in `config/pipeline_config.yaml`.

## License

The code in `code/` and the script `verify_poc_numbers.py` are distributed under the MIT License (`LICENSE`). The data, reports, and documentation are distributed under the Creative Commons Attribution 4.0 International License (`LICENSE-DATA`).

## Citation

[TODO: citation of the paper and DOI of the Zenodo archive]
