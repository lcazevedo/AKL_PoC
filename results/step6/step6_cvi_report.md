# EVoC CVI Analysis Report
Generated: 2026-11-04 16:54:47

**Alpha estimated via Linear Regression:** -2.8463

## Metrics per Layer
|   Layer |   N_Topics | Named   |   Silhouette |   Davies_Bouldin |    Q_score |   CVI1_Sqrt |    CVI2_Adaptive |
|--------:|-----------:|:--------|-------------:|-----------------:|-----------:|------------:|-----------------:|
|       0 |       1117 | False   |    0.0193592 |          3.53803 | 0.495385   | 0.0148223   |      2.34804e+08 |
|       1 |        346 | False   |    0.0285146 |          3.55697 | 0.484381   | 0.0260405   |      8.17021e+06 |
|       2 |        145 | False   |    0.0304866 |          3.52034 | 0.515243   | 0.0427886   | 731100           |
|       3 |         60 | True    |    0.0300479 |          3.7593  | 0.319818   | 0.0412883   |  36821.9         |
|       4 |         14 | True    |    0.0276523 |          4.09244 | 0.0475686  | 0.0127132   |     87.0117      |
|       5 |          5 | True    |    0.0337874 |          4.1508  | 8.1987e-10 | 3.66657e-10 |      8.00283e-08 |

## Recommendations
- **CVI 1 (Sqrt)** suggests Layer: **2**
- **CVI 2 (Adaptive)** suggests Layer: **0**
- **Kneedle Algorithm** suggests Layer: **2**

⚠️ **NO CONSENSUS.** The metrics diverged. Please check the `step6_kneedle_plot.png` and 2D maps to decide which layer to select based on your research goals.
