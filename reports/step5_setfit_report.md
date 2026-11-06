# SetFit Training Quality Report
Generated: 2026-11-04 16:08:38

## Summary Metrics
- **Global Accuracy**: 0.7403
- **Macro F1-Score**: 0.7300

## Classification Report
```text
              precision    recall  f1-score   support

          no       0.61      0.76      0.68        55
         yes       0.85      0.73      0.78        99

    accuracy                           0.74       154
   macro avg       0.73      0.75      0.73       154
weighted avg       0.76      0.74      0.75       154

```

## Confusion Matrix
| | Predicted Yes | Predicted No |
|---|---|---|
| **Actual Yes** | 72 | 27 |
| **Actual No** | 13 | 42 |

## Interpretation of AI_Confidence
The `AI_Confidence` column added to the `.xlsx` inspection files represents the SetFit model's certainty in its prediction (ranging from roughly 0.5 to 1.0). 
- Values close to **1.0** indicate high certainty.
- Values closer to **0.5** indicate the model was unsure if the document was relevant or not. 
You can sort the Excel files by this column to review the documents the AI struggled with the most.

## Settings
- Base model: `all-MiniLM-L6-v2`
- Epochs: 1 | batch size: 16 | num_iterations: 10 (oversampling)
- Head class_weight: `balanced`
- Decision threshold on P(yes): **0.5**

## Retention Check (Reviewer Validation #4)
The trained model was re-applied to all 569 documents labeled by the
specialist in Step 4 (344 relevant, 225 not relevant) to verify it retains the
expert's labels.

- **Retention accuracy**: 0.9297
- **Split method**: GroupShuffleSplit (grouped by Step-3 topic) — no topic-level leakage
- **Train / Test**: 415 / 154 documents

A retention accuracy well below the eval accuracy may indicate overfitting to the
test split or label noise; investigate before trusting the corpus filter.
