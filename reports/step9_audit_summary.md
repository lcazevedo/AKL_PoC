## Validation & Audit Summary

This section summarizes the reviewer-requested validations performed during the pipeline run.

### Topic-Size Verification (Step 6)
- Not performed.


### Classification Audits (Step 8)

No audit report found.


### Automated Audits (Step 8)

#### EVoC Sensitivity (reviewer #5)

Pairwise Adjusted Rand Index (ARI) between the EVoC layers computed in Step 6. ARI > 0.7 indicates stable clustering across resolutions; 0.3–0.7 moderate; < 0.3 sensitive (the layer choice materially changes the topic map).

| Layer pair | Topics (A → B) | ARI |
|---|---|---|
| Layer 3 vs Layer 4 | 60 → 14 | 0.292 |
| Layer 3 vs Layer 5 | 60 → 5 | 0.094 |
| Layer 4 vs Layer 5 | 14 → 5 | 0.367 |

#### Regression Audit (reviewer #9)

OLS of log1p(citation_count) on Step-6 topics (top 10 + Other), centered year, and journal IF (with missingness dummy). n = 47905 documents, k = 14 predictors.

| Predictor | Coef | SE | Bootstrap 95% CI |
|---|---|---|---|
| topic_16_Electrocatalysis | 0.435 | 0.043 | [0.349, 0.521] |
| topic_21_Methane Catalysis | 0.029 | 0.045 | [-0.054, 0.108] |
| topic_26_Phonon Thermoelectricity | 0.402 | 0.047 | [0.309, 0.493] |
| topic_29_Materials Prediction | 0.596 | 0.046 | [0.498, 0.693] |
| topic_30_Generative Materials | 0.496 | 0.046 | [0.401, 0.596] |
| topic_45_Composite Laminates | 0.300 | 0.043 | [0.219, 0.383] |
| topic_50_Atomistic Modeling | 0.254 | 0.046 | [0.180, 0.340] |
| topic_54_Atomistic Potentials | 0.796 | 0.048 | [0.703, 0.900] |
| topic_8_Lithium Electrolytes | 0.273 | 0.047 | [0.184, 0.366] |
| topic_Other | 0.360 | 0.032 | [0.302, 0.424] |
| year_c | -0.160 | 0.001 | [-0.163, -0.157] |
| if_filled | 0.064 | 0.001 | [0.061, 0.066] |
| if_missing | -0.795 | 0.020 | [-0.838, -0.748] |
| const | 1.457 | 0.032 | [1.396, 1.514] |

Kruskal-Wallis across topics: H = 122.54, p = 0.0000 (p < 0.05 → citation counts differ across topics).

Robustness (drop journal IF): max |Δcoef| = 0.370 across shared predictors (small → coefficients stable).

#### Growth Model Fitting (reviewer #11)

Formal model selection per macro-category: Plateau (constant), Linear, or Exponential (log-linear), chosen by minimum AICc. ΔAICc < 2 → models are statistically indistinguishable. The heuristic recent-ratio is kept for continuity with the original classification.

| macro_category                       |   n_years |   total_mentions |   recent_ratio | best_model   |   AICc |   ΔAICc vs 2nd |
|:-------------------------------------|----------:|-----------------:|---------------:|:-------------|-------:|---------------:|
| Dft Or Simulation                    |        27 |            19303 |           0.57 | Exponential  |   21.2 |         -418.6 |
| Computational Benchmark              |        27 |            19233 |           0.56 | Exponential  |   25   |         -414.2 |
| Experimental Validation              |        27 |            18891 |           0.55 | Exponential  |   23.7 |         -414.4 |
| Material Property Prediction         |        27 |            18471 |           0.55 | Exponential  |   23.4 |         -411.8 |
| Machine Learning for Chemistry       |        26 |            14337 |           0.67 | Exponential  |   50.5 |         -371.9 |
| Experiments                          |        27 |            13072 |           0.52 | Exponential  |   21.1 |         -392.2 |
| Neural Network Methods               |        27 |             9359 |           0.47 | Exponential  |   26.8 |         -359.8 |
| Process and Design Optimization      |        27 |             8602 |           0.52 | Exponential  |   18.8 |         -372.3 |
| Future Research Directions           |        27 |             7154 |           0.63 | Exponential  |   54.4 |         -339.3 |
| Data Limitations                     |        27 |             6429 |           0.63 | Exponential  |   60.5 |         -331.9 |
| Metallic Alloys and Systems          |        27 |             6056 |           0.57 | Exponential  |   35.9 |         -343.3 |
| Challenging Application Contexts     |        27 |             5457 |           0.69 | Exponential  |   46.3 |         -347.8 |
| Material Properties                  |        27 |             5271 |           0.59 | Exponential  |   34.7 |         -339.9 |
| Mechanical Properties                |        27 |             5152 |           0.58 | Exponential  |   26.6 |         -345   |
| Accurate Property Prediction         |        27 |             4771 |           0.5  | Exponential  |   25.9 |         -327.1 |
| Project Costs and Resources          |        27 |             4685 |           0.63 | Exponential  |   52.2 |         -321.5 |
| Cross-Validation Only                |        27 |             4550 |           0.55 | Exponential  |   34.9 |         -328.4 |
| Evolutionary and Swarm Optimization  |        27 |             4426 |           0.26 | Exponential  |   -9.6 |         -275   |
| Material Performance Characteristics |        27 |             4384 |           0.57 | Exponential  |   29.6 |         -331.9 |
| Machine Learning in Chemistry        |        25 |             4252 |           0.66 | Exponential  |   70.8 |         -274.3 |

#### Relevance Index Sensitivity (reviewer #10)

Skipped: no Relevance Index column is computed in this pipeline (RI is not standard in AKL). If RI is added later, this audit will verify the unit-invariance of the ranking.

Full report: `data/04_reports/step8_data_crunching.md`
