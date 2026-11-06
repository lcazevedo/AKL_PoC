# Log of analytic decisions

Proof of concept: machine learning in chemistry and materials science.

This log lists the analytic decisions taken during the execution after inspecting the data or intermediate outputs. For each decision, it gives the step, the reason, and the effect on what is reported.

| # | Step | Decision | Reason | Note |
|---|---|---|---|---|
| 1 | 4 | Active expansion of the not-relevant labels in two rounds (53 → 167 → 225), with candidates pre-labeled by the local extraction model and validated by the expert | The preliminary topics contained few not-relevant documents, which left the classifier with an unbalanced training set | Final set: 569 labels (344 relevant, 225 not relevant) |
| 2 | 2 | The language of the abstract prevails when the metadata language and the detected language diverge | The language rule discarded about 500 articles written in English | Approved by the expert |
| 3 | 6 | Layer 3 (60 topics) selected at the Step 6 breakpoint | The indices did not agree. The Standard CVI and Kneedle indicated layer 2 (145 topics), above the naming limit of 100 topics, and the Adaptive CVI indicated layer 0 with a negative decay factor (α = -2.85) | Deviation from the selection rule defined before the execution. The Standard CVI of layer 3 (0.0413) was close to that of layer 2 (0.0428) |
| 4 | 7 | Fixed lists of answers for vectors with few labels (`validation`, `data_source`) | The automatic naming of clusters mixed categories of these vectors | The labels are used directly as categories |
| 5 | 7 | Keyword pre-filter for sentences disabled | In a pilot on 300 documents, it kept 40% of the sentences but lost 28% to 44% of the positive labels | |
| 6 | 7 | Vector `readiness` deactivated | In the pilot, 282 of 300 documents fell in "proof of concept", and after a redefinition 7% of the documents were labeled as laboratory use, which the samples showed to be implausible (the labels confused experimental validation with laboratory use) | Readiness is read through the `validation` vector |
| 7 | 7 | LLM yes/no sentence verifier adopted for challenges and directions, with thresholds 0.2 and 0.5 | The audit of the direction labels gave an accuracy of 0.39, and most errors were sentences that did not state a direction | The prompt and the thresholds were chosen on the audited sentences, so the post-verification estimates are optimistic. An alternative sentence classifier was tested and not adopted |
| 8 | 8 | Extraction audits (challenges and directions) pre-reviewed by the orchestration agent before the expert's decision | To speed up the annotation | Possible anchoring bias. A blind annotation round is planned |
| 9 | 5, 8 | Decision-boundary audit of the relevance filter not run | No expert-labeled sample had been drawn from the uncertainty band of the reported filter | The 805 documents with 0.40 ≤ P(relevant) ≤ 0.60 were exported for review. Their audit is left to a blind relevance sample planned for the next iteration |
| 10 | 8 | Rule for the regime of the topics rewritten (comparison also with 2014-2016, threshold for "still growing" raised from 1.05 to 1.10) | The initial rule labeled as "rising" topics whose curve was clearly declining | Changed after inspecting the figures. The final rule and the variants are reported in the Step 8 outputs. The regime of the topics is not reported in the paper |
