# Step 8: Statistical Data Crunching Report

> This report contains computed cienciometric matrices. The LLM agent will use this to generate the final qualitative synthesis.

## 1. Thematic Lifecycle (Growth Regimes)
Classifies research categories based on their volume concentration in the last 3 years.

| macro_category                       |   total_mentions |   recent_ratio | growth_regime        |
|:-------------------------------------|-----------------:|---------------:|:---------------------|
| Dft Or Simulation                    |            19303 |           0.57 | Exponential/Emerging |
| Computational Benchmark              |            19233 |           0.56 | Exponential/Emerging |
| Experimental Validation              |            18891 |           0.55 | Exponential/Emerging |
| Material Property Prediction         |            18471 |           0.55 | Exponential/Emerging |
| Machine Learning for Chemistry       |            14337 |           0.67 | Exponential/Emerging |
| Experiments                          |            13072 |           0.52 | Exponential/Emerging |
| Neural Network Methods               |             9359 |           0.47 | Linear/Mainstream    |
| Process and Design Optimization      |             8602 |           0.52 | Exponential/Emerging |
| Future Research Directions           |             7154 |           0.63 | Exponential/Emerging |
| Data Limitations                     |             6429 |           0.63 | Exponential/Emerging |
| Metallic Alloys and Systems          |             6056 |           0.57 | Exponential/Emerging |
| Challenging Application Contexts     |             5457 |           0.69 | Exponential/Emerging |
| Material Properties                  |             5271 |           0.59 | Exponential/Emerging |
| Mechanical Properties                |             5152 |           0.58 | Exponential/Emerging |
| Accurate Property Prediction         |             4771 |           0.5  | Linear/Mainstream    |
| Project Costs and Resources          |             4685 |           0.63 | Exponential/Emerging |
| Cross-Validation Only                |             4550 |           0.55 | Exponential/Emerging |
| Evolutionary and Swarm Optimization  |             4426 |           0.26 | Linear/Mainstream    |
| Material Performance Characteristics |             4384 |           0.57 | Exponential/Emerging |
| Machine Learning in Chemistry        |             4252 |           0.66 | Exponential/Emerging |

## 2. Strategic Geopolitics (Pioneers vs Traditionalists)
Row-normalized proportion of a country's effort dedicated to Exponential/Emerging vs Plateau/Mainstream themes.

| first_country   |   Exponential/Emerging |   Linear/Mainstream |
|:----------------|-----------------------:|--------------------:|
| Australia       |                   92.5 |                 7.5 |
| Canada          |                   90.9 |                 9.1 |
| China           |                   92   |                 8   |
| France          |                   89.1 |                10.9 |
| Germany         |                   88.8 |                11.2 |
| India           |                   90.8 |                 9.2 |
| Iran            |                   87   |                13   |
| Italy           |                   88.5 |                11.5 |
| Japan           |                   89.5 |                10.5 |
| South Korea     |                   92.1 |                 7.9 |
| Spain           |                   88.1 |                11.9 |
| Switzerland     |                   86.6 |                13.4 |
| United Kingdom  |                   88.1 |                11.9 |
| United States   |                   89.7 |                10.3 |
| Unknown         |                   86.7 |                13.3 |

## 3. Bottleneck Regimes & Semantic Clustering
#### Bottleneck Regime: CHALLENGES vs Topics (Row-Normalized %)
| Topic ID                |   Complex Parameter Optimization |   Computational Complexity |   Data Limitations |   Data and Method Limitations |   Machine Learning in Chemistry |   Model Limitations & Data |   Modeling and Validation Challenges |   Research Reproducibility Challenges |
|:------------------------|---------------------------------:|---------------------------:|-------------------:|------------------------------:|--------------------------------:|---------------------------:|-------------------------------------:|--------------------------------------:|
| 16_Electrocatalysis     |                              6.3 |                        8.9 |               17.3 |                          10.1 |                            20.9 |                       10.1 |                                 10.6 |                                  15.7 |
| 22_Catalysis            |                              5.8 |                       14.5 |               25.3 |                           8   |                            15.9 |                       14.2 |                                  6.7 |                                   9.5 |
| 29_Materials Prediction |                              4.8 |                        4.5 |               42.1 |                           5.9 |                            14.7 |                       19   |                                  3.4 |                                   5.6 |
| 30_Generative Materials |                              7.9 |                       10   |               36.7 |                           8.6 |                            11.6 |                       12.6 |                                  5.4 |                                   7.1 |
| 45_Composite Laminates  |                              6.8 |                       11.5 |               31.3 |                           6.6 |                            14.7 |                       14.9 |                                  5.5 |                                   8.6 |
| 52_Polymer Chemistry    |                              7.1 |                        5.7 |               41.6 |                           6.2 |                            14.4 |                       14.6 |                                  3.9 |                                   6.5 |
| 54_Atomistic Potentials |                              7.9 |                       17.9 |               25.7 |                           7.1 |                            17.8 |                        6.3 |                                  8.3 |                                   9   |
| 55_Molecular Solvation  |                             10.5 |                       16.5 |               24.3 |                           8.7 |                            14.8 |                       10.3 |                                  7.3 |                                   7.5 |
| 59_Molecular Synthesis  |                              5.6 |                        4.9 |               39.1 |                           8.6 |                            11.3 |                       18.7 |                                  4.1 |                                   7.8 |
| 8_Lithium Electrolytes  |                              4.3 |                       10.6 |               21.8 |                          11   |                            15.8 |                        7.6 |                                 11.5 |                                  17.5 |

#### Bottleneck Regime: BEST_PRACTICES vs Topics (Row-Normalized %)
| Topic ID                 |   Curated Data Practices |   Data Management Practices |   Experimental Best Practices |   Experimental Design & Optimization |   Model Optimization Strategies |   Model Validation & Analysis |   Uncertainty and Interpretability |   Validation and Verification |
|:-------------------------|-------------------------:|----------------------------:|------------------------------:|-------------------------------------:|--------------------------------:|------------------------------:|-----------------------------------:|------------------------------:|
| 14_Molecular Descriptors |                      9.4 |                         6.4 |                           3.3 |                                  7   |                            33.4 |                           7.3 |                                8.1 |                          25   |
| 16_Electrocatalysis      |                      9.1 |                         6.1 |                          14.9 |                                  7.6 |                            16.7 |                           9.1 |                                7.1 |                          29.4 |
| 21_Methane Catalysis     |                      5.8 |                         5.8 |                           5   |                                  9.7 |                            19.2 |                          16.8 |                                8.4 |                          29.4 |
| 29_Materials Prediction  |                     29   |                         7.3 |                          10.8 |                                  6.1 |                             9.3 |                           2.8 |                               20.3 |                          14.4 |
| 37_Magnesium Alloys      |                      7.6 |                         6.5 |                           4.1 |                                  7.9 |                            29   |                          10.3 |                                8.7 |                          26   |
| 43_Austenite Steel       |                      9   |                         9.7 |                           3.2 |                                  8.1 |                            24.3 |                           6.7 |                               14.4 |                          24.5 |
| 45_Composite Laminates   |                      3.6 |                         5   |                           6.4 |                                 11.2 |                            20   |                          12.3 |                               11.1 |                          30.3 |
| 49_Alloy Thermodynamics  |                      8.1 |                         6.3 |                           5.8 |                                  4.2 |                            23.9 |                           7.9 |                               13.6 |                          30.2 |
| 52_Polymer Chemistry     |                     15.1 |                         8.9 |                           6.4 |                                  6.2 |                            20.8 |                           7.8 |                               11.2 |                          23.7 |
| 54_Atomistic Potentials  |                      8.5 |                         4.8 |                           5.9 |                                  5.9 |                            22.7 |                           4.5 |                               30.1 |                          17.6 |

#### Bottleneck Regime: ML_METHODS vs Topics (Row-Normalized %)
| Topic ID                 |   Deep Learning for Materials |   Evolutionary and Swarm Optimization |   Graph and Deep Neural Networks |   Machine Learning Methods |   Machine Learning for Chemistry |   Neural Network Methods |   Regression and Classification Methods |   Statistical Modeling & Analysis |
|:-------------------------|------------------------------:|--------------------------------------:|---------------------------------:|---------------------------:|---------------------------------:|-------------------------:|----------------------------------------:|----------------------------------:|
| 14_Molecular Descriptors |                           3.1 |                                   9.9 |                              3.6 |                        9.9 |                             20.8 |                     32   |                                    12.6 |                               8.1 |
| 16_Electrocatalysis      |                           2   |                                   4.2 |                              2   |                        2.1 |                             71.3 |                      8.3 |                                     7.8 |                               2.1 |
| 21_Methane Catalysis     |                           1.7 |                                  30.3 |                              1.4 |                        6.4 |                             20.7 |                     30.4 |                                     5.3 |                               3.8 |
| 22_Catalysis             |                           4.1 |                                   6.6 |                              2.6 |                        3.9 |                             50.9 |                     18.6 |                                     7.5 |                               5.7 |
| 29_Materials Prediction  |                           9.2 |                                   2.3 |                              2.2 |                        3   |                             69.1 |                      7.3 |                                     3.7 |                               3.4 |
| 30_Generative Materials  |                          15.8 |                                   6.2 |                             11.5 |                        3   |                             25.5 |                     30.5 |                                     3.5 |                               4   |
| 37_Magnesium Alloys      |                           3.2 |                                   9.8 |                              2.3 |                       11.6 |                             24.5 |                     32.5 |                                    11   |                               4.9 |
| 43_Austenite Steel       |                           4.1 |                                   8.6 |                              6.4 |                        8.7 |                             20.5 |                     37.6 |                                     9.4 |                               4.7 |
| 45_Composite Laminates   |                           9.2 |                                  11.8 |                              8.4 |                        6.9 |                             18.6 |                     33.4 |                                     5.9 |                               5.8 |
| 50_Atomistic Modeling    |                           6.6 |                                   6.8 |                              5   |                        2   |                             46.6 |                     25.5 |                                     3.8 |                               3.9 |

#### Bottleneck Regime: VALIDATION vs Topics (Row-Normalized %)
| Topic ID                    |   Computational Benchmark |   Cross-Validation Only |   Experimental Validation |   No Validation |
|:----------------------------|--------------------------:|------------------------:|--------------------------:|----------------:|
| 14_Molecular Descriptors    |                      32.1 |                    35.4 |                      30.4 |             2   |
| 16_Electrocatalysis         |                      64.7 |                     3   |                      29.1 |             3.3 |
| 21_Methane Catalysis        |                      34.8 |                     6.3 |                      53.6 |             5.3 |
| 26_Phonon Thermoelectricity |                      68.4 |                     3.6 |                      27.4 |             0.6 |
| 30_Generative Materials     |                      54.3 |                    13.4 |                      29.1 |             3.2 |
| 37_Magnesium Alloys         |                      16.9 |                    12.2 |                      68.8 |             2.1 |
| 43_Austenite Steel          |                      27.2 |                    14.4 |                      55.7 |             2.7 |
| 45_Composite Laminates      |                      23.5 |                    12.5 |                      61.9 |             2.2 |
| 50_Atomistic Modeling       |                      64.9 |                     3.7 |                      30.9 |             0.6 |
| 8_Lithium Electrolytes      |                      57.9 |                     5.1 |                      36.2 |             0.8 |

#### Bottleneck Regime: FINDINGS vs Topics (Row-Normalized %)
| Topic ID                    |   Accurate Property Prediction |   Advanced Material Design |   Enhanced Performance and Speed |   Material Property Characterization |   Materials Discovery & Validation |   Materials Modeling Advancements |   Prediction Accuracy Improvements |   Process and Design Optimization |
|:----------------------------|-------------------------------:|---------------------------:|---------------------------------:|-------------------------------------:|-----------------------------------:|----------------------------------:|-----------------------------------:|----------------------------------:|
| 14_Molecular Descriptors    |                           38.7 |                        1.6 |                              9.5 |                                  0.6 |                               11   |                              13.9 |                               19.9 |                               4.8 |
| 18_Metasurfaces             |                            5   |                        2.7 |                             14.5 |                                 35.3 |                                5   |                              11.8 |                                8.7 |                              17.1 |
| 20_Nanoalloys               |                            2.6 |                       47.2 |                              3.3 |                                  7.1 |                               22.1 |                               9.1 |                                0.7 |                               8   |
| 26_Phonon Thermoelectricity |                           13.8 |                       20.1 |                              7.9 |                                 32.8 |                               10.8 |                               5.4 |                                5.4 |                               3.9 |
| 30_Generative Materials     |                           17.6 |                       17.3 |                             12.4 |                                  3.6 |                                8.5 |                              18.6 |                               16   |                               5.8 |
| 37_Magnesium Alloys         |                           25.4 |                       23.5 |                             10.4 |                                  2.2 |                                5.5 |                               6.5 |                               12.1 |                              14.4 |
| 43_Austenite Steel          |                           34.3 |                       14.8 |                              8.5 |                                  0.7 |                                7.1 |                               7.4 |                               15   |                              12.2 |
| 45_Composite Laminates      |                           24.8 |                        4.4 |                             11.3 |                                  2   |                                6.5 |                              13.5 |                               15.9 |                              21.6 |
| 50_Atomistic Modeling       |                           16.7 |                       33.9 |                              6.4 |                                  5.8 |                               12.6 |                              10.5 |                                8.1 |                               6.1 |
| 54_Atomistic Potentials     |                           10.3 |                       12.7 |                             13.7 |                                  6.3 |                                9.9 |                              19.2 |                               15   |                              13   |

#### Bottleneck Regime: BENCHMARKS_DATASETS vs Topics (Row-Normalized %)
| Topic ID                   |   Existing Materials Data |   Materials Data & Models |   Materials Data Repositories |   Materials Science Datasets |   Materials Structure Databases |   Molecular and Materials Data |   Publicly Available Datasets |   Quantum Chemistry Datasets |
|:---------------------------|--------------------------:|--------------------------:|------------------------------:|-----------------------------:|--------------------------------:|-------------------------------:|------------------------------:|-----------------------------:|
| 12_Battery Prediction      |                       3.2 |                       3.6 |                          28   |                          0.4 |                             0.4 |                            5.2 |                          46.4 |                         12.8 |
| 14_Molecular Descriptors   |                      12.4 |                       4.7 |                          30.2 |                          0.6 |                             1.8 |                           20.7 |                          23.1 |                          6.5 |
| 25_Neuromorphic Memristors |                       0   |                      66.1 |                          24.1 |                          0   |                             0   |                            1.8 |                           5.4 |                          2.7 |
| 29_Materials Prediction    |                      11.6 |                       5.8 |                          20.6 |                         23.9 |                            14.2 |                            7.1 |                          15.5 |                          1.3 |
| 30_Generative Materials    |                       7   |                       4.4 |                          21.9 |                         27.3 |                            13.9 |                           12.1 |                           6.2 |                          7.2 |
| 52_Polymer Chemistry       |                      13   |                       4.6 |                          24.1 |                          1.9 |                            14.8 |                           12   |                          23.1 |                          6.5 |
| 54_Atomistic Potentials    |                       3.3 |                       5   |                          25.6 |                          8.9 |                             6.1 |                           24.4 |                          11.1 |                         15.6 |
| 55_Molecular Solvation     |                       1.3 |                       1.3 |                          27.1 |                          1.9 |                             3.2 |                           41.3 |                           3.9 |                         20   |
| 56_Molecular Prediction    |                       6.1 |                       1   |                          22.2 |                          1   |                             2   |                           21.7 |                          10.1 |                         35.9 |
| 59_Molecular Synthesis     |                       8   |                       2.5 |                          20.9 |                          1.5 |                             9.5 |                           31.8 |                          16.9 |                          9   |

#### Bottleneck Regime: APPLICATION_TASK vs Topics (Row-Normalized %)
| Topic ID                 |   Catalysis and Electrocatalysis |   Computational Structure Modeling |   Environmental Separation and Treatment |   Material Analysis and Assessment |   Material Property Prediction |   Materials Design & Optimization |   Materials Property Investigation |   Process and Design Optimization |
|:-------------------------|---------------------------------:|-----------------------------------:|-----------------------------------------:|-----------------------------------:|-------------------------------:|----------------------------------:|-----------------------------------:|----------------------------------:|
| 14_Molecular Descriptors |                              0.1 |                                1.2 |                                      3.1 |                                7.7 |                           78.7 |                               2.5 |                                1   |                               5.7 |
| 16_Electrocatalysis      |                             82.5 |                                0.2 |                                      3.1 |                                0.6 |                            8.5 |                               0.2 |                                0.8 |                               4   |
| 21_Methane Catalysis     |                             27.7 |                                0   |                                     11.5 |                                0.9 |                            3.4 |                               1.6 |                                0.1 |                              54.9 |
| 22_Catalysis             |                             73.6 |                                2.4 |                                      0.2 |                                4.4 |                           13.5 |                               1   |                                1.3 |                               3.6 |
| 30_Generative Materials  |                              0.2 |                               24.4 |                                      0.1 |                                5.7 |                           51.9 |                               5.3 |                                9.7 |                               2.7 |
| 37_Magnesium Alloys      |                              0   |                                0.2 |                                      0.4 |                                1.3 |                           54.9 |                              15.3 |                                8.6 |                              19.5 |
| 43_Austenite Steel       |                              0   |                                0.2 |                                      3.6 |                                2.1 |                           59.7 |                              11.3 |                                5.8 |                              17.4 |
| 45_Composite Laminates   |                              0   |                                0.1 |                                      1.9 |                               11.4 |                           52   |                               4.1 |                                7.9 |                              22.6 |
| 50_Atomistic Modeling    |                              0.3 |                                8   |                                      2.6 |                                3.4 |                           54   |                               8.8 |                               18.2 |                               4.7 |
| 54_Atomistic Potentials  |                              0.5 |                               48.5 |                                      0.5 |                                2.5 |                           33.3 |                               3.1 |                                6.1 |                               5.4 |

#### Bottleneck Regime: MATERIAL_SYSTEM vs Topics (Row-Normalized %)
| Topic ID                    |   Advanced Battery Technologies |   Advanced Functional Materials |   Metallic Alloys and Systems |   Molecular and Chemical Materials |   Oxide-Based Perovskite Materials |   Polymeric Materials |   Porous Coordination Networks |   Solid-State Materials |
|:----------------------------|--------------------------------:|--------------------------------:|------------------------------:|-----------------------------------:|-----------------------------------:|----------------------:|-------------------------------:|------------------------:|
| 11_Lithium Batteries        |                            74.7 |                             3.8 |                           2.1 |                                0.8 |                                9   |                   0.7 |                            4   |                     4.9 |
| 12_Battery Prediction       |                            95.6 |                             0.2 |                           0   |                                0   |                                0.2 |                   0.1 |                            3.6 |                     0.2 |
| 16_Electrocatalysis         |                             6.8 |                            19.7 |                          27.9 |                                7.1 |                               13.5 |                   0.6 |                           17.1 |                     7.3 |
| 26_Phonon Thermoelectricity |                             0.3 |                            41.2 |                           6.2 |                                2.7 |                               13.3 |                   0.1 |                           12.7 |                    23.5 |
| 30_Generative Materials     |                             1.6 |                             8.7 |                           6.2 |                                9.3 |                               10.7 |                   0.7 |                            6.9 |                    55.7 |
| 37_Magnesium Alloys         |                             0.3 |                             0.9 |                          89.3 |                                0   |                                3.4 |                   0.1 |                            2.1 |                     3.9 |
| 49_Alloy Thermodynamics     |                             0   |                             1.4 |                          82.3 |                                0.4 |                                2.3 |                   0   |                            9.9 |                     3.8 |
| 50_Atomistic Modeling       |                             0.1 |                             4.8 |                          58.9 |                                0.7 |                                6.2 |                   0   |                            8.8 |                    20.5 |
| 52_Polymer Chemistry        |                             0   |                             0.7 |                           0.2 |                                2.6 |                                0.2 |                  94.3 |                            1.1 |                     1   |
| 8_Lithium Electrolytes      |                            72.6 |                             4.7 |                           0.8 |                                1.4 |                                6.3 |                   1.8 |                            5.7 |                     6.7 |

#### Bottleneck Regime: TARGET_PROPERTY vs Topics (Row-Normalized %)
| Topic ID                    |   Material Performance Characteristics |   Material Properties |   Material Properties and Structure |   Mechanical Properties |   Optical and Vibrational Properties |   Property Performance Metrics |   Reaction and Catalysis Properties |   Thermodynamic and Energetic Properties |
|:----------------------------|---------------------------------------:|----------------------:|------------------------------------:|------------------------:|-------------------------------------:|-------------------------------:|------------------------------------:|-----------------------------------------:|
| 16_Electrocatalysis         |                                   18.9 |                  11.1 |                                 2.7 |                     1.1 |                                  0.8 |                           22.8 |                                32.8 |                                      9.8 |
| 18_Metasurfaces             |                                   11.5 |                   2.5 |                                 7   |                     1   |                                 61.6 |                           15.9 |                                 0.3 |                                      0.4 |
| 20_Nanoalloys               |                                   17.6 |                   7.1 |                                32   |                     4.2 |                                  7.6 |                            0.4 |                                 3.5 |                                     27.7 |
| 26_Phonon Thermoelectricity |                                   10.4 |                  64.5 |                                 3.8 |                     8   |                                  7.3 |                            2.4 |                                 0.4 |                                      3.2 |
| 30_Generative Materials     |                                   13.3 |                  10.5 |                                33.9 |                     6.1 |                                  9.6 |                            0.8 |                                 4.6 |                                     21.2 |
| 37_Magnesium Alloys         |                                   16.2 |                  30.5 |                                 3.2 |                    47.3 |                                  0.3 |                            1.4 |                                 0.5 |                                      0.5 |
| 43_Austenite Steel          |                                   13.2 |                  23.6 |                                 2.8 |                    55.4 |                                  0.3 |                            1.4 |                                 0.8 |                                      2.6 |
| 45_Composite Laminates      |                                   11.6 |                   8.2 |                                 4.6 |                    66.6 |                                  1.8 |                            4.2 |                                 1   |                                      2   |
| 50_Atomistic Modeling       |                                    7.7 |                  13.6 |                                10.5 |                    37.5 |                                  1.1 |                            0.9 |                                 2.9 |                                     25.8 |
| 8_Lithium Electrolytes      |                                    8.1 |                  58.9 |                                 4.2 |                     7.6 |                                  0.5 |                            8.8 |                                 6.3 |                                      5.6 |

#### Bottleneck Regime: DATA_SOURCE vs Topics (Row-Normalized %)
| Topic ID                    |   Dft Or Simulation |   Experiments |   Industrial Data |   Literature Text Mining |   Mixed |   Public Database |
|:----------------------------|--------------------:|--------------:|------------------:|-------------------------:|--------:|------------------:|
| 14_Molecular Descriptors    |                28.6 |          52.4 |               0.4 |                     12.3 |     3.1 |               3.1 |
| 16_Electrocatalysis         |                75.5 |          13   |               0   |                      6.8 |     4.4 |               0.3 |
| 21_Methane Catalysis        |                13.4 |          67.5 |               4.5 |                     11.3 |     3   |               0.3 |
| 22_Catalysis                |                78   |          13.3 |               0   |                      4.1 |     3.9 |               0.8 |
| 26_Phonon Thermoelectricity |                88.1 |           7   |               0   |                      1.4 |     2.4 |               1.1 |
| 30_Generative Materials     |                65.8 |          16.8 |               0   |                      4.5 |     4.7 |               8.2 |
| 45_Composite Laminates      |                20.7 |          71.3 |               0.7 |                      2.8 |     4.1 |               0.4 |
| 50_Atomistic Modeling       |                89.8 |           7.1 |               0   |                      0.7 |     2.1 |               0.2 |
| 54_Atomistic Potentials     |                95.4 |           2.4 |               0   |                      0.2 |     1.4 |               0.6 |
| 8_Lithium Electrolytes      |                74.4 |          14   |               0   |                      4.6 |     5.9 |               1.1 |

#### Bottleneck Regime: APPLICATION_CHALLENGES vs Topics (Row-Normalized %)
| Topic ID                 |   Challenging Application Contexts |   Complex System Challenges |   Experimental and Modeling Complexities |   Industrial Translation |   Practical Applications & Design |   Process and Materials Challenges |   Project Costs and Resources |   Synthesis and Scale-Up |
|:-------------------------|-----------------------------------:|----------------------------:|-----------------------------------------:|-------------------------:|----------------------------------:|-----------------------------------:|------------------------------:|-------------------------:|
| 10_Nanoporous MOFs       |                               20.8 |                         6   |                                      4.8 |                      9.8 |                               8.6 |                               18.8 |                          13.7 |                     17.5 |
| 11_Lithium Batteries     |                               12.6 |                         7.8 |                                      9.3 |                     22.4 |                              10   |                               11.1 |                          15.3 |                     11.5 |
| 12_Battery Prediction    |                               32.5 |                         7   |                                     18.2 |                      7.2 |                              17   |                                3.4 |                           6.2 |                      8.5 |
| 14_Molecular Descriptors |                               20   |                        10   |                                      9.8 |                     10.4 |                               9.7 |                               18.2 |                          11.5 |                     10.4 |
| 16_Electrocatalysis      |                               16.8 |                         5.6 |                                      5   |                     14.1 |                               7.7 |                               16.7 |                          20.3 |                     13.9 |
| 1_Chemical Sensing       |                               25.6 |                        15.7 |                                     10.5 |                      6.2 |                              13.5 |                               10.6 |                           8.5 |                      9.3 |
| 21_Methane Catalysis     |                               20.5 |                         4.6 |                                      9   |                     19.9 |                               7.8 |                               20.5 |                           9.7 |                      8   |
| 45_Composite Laminates   |                               11.9 |                        12.9 |                                     15.4 |                     14.3 |                              15.1 |                                5.1 |                          14.2 |                     11.2 |
| 6_Photocatalysis         |                               33.5 |                         4.2 |                                      8.7 |                     10.3 |                               6.6 |                               17.8 |                           8.3 |                     10.6 |
| 8_Lithium Electrolytes   |                               10.9 |                         8.6 |                                      8.5 |                     12   |                               9   |                               23.5 |                          14.1 |                     13.4 |

#### Bottleneck Regime: DIRECTIONS vs Topics (Row-Normalized %)
| Topic ID                |   AI-Driven Materials Science |   Computational Catalyst Design |   Computational Materials Design |   Computational Multiscale Modeling |   Future Research Directions |   Materials Design & Discovery |   Methodological Advancements |   Optimization Strategies |
|:------------------------|------------------------------:|--------------------------------:|---------------------------------:|------------------------------------:|-----------------------------:|-------------------------------:|------------------------------:|--------------------------:|
| 10_Nanoporous MOFs      |                           7.9 |                            12.3 |                             15.1 |                                 3.6 |                         27.3 |                           22.9 |                           5.7 |                       5.1 |
| 11_Lithium Batteries    |                           6.6 |                             3.5 |                             12   |                                 5.5 |                         39.1 |                           18.6 |                           8.5 |                       6.2 |
| 16_Electrocatalysis     |                           6.4 |                            22   |                             18.9 |                                 3.2 |                         33   |                            7.9 |                           4.9 |                       3.7 |
| 22_Catalysis            |                           7.3 |                            19.7 |                             18   |                                 6.6 |                         31.6 |                            5.9 |                           7.6 |                       3.4 |
| 29_Materials Prediction |                          12.6 |                             1.1 |                              8.1 |                                 2.3 |                         39.5 |                           22.2 |                          11.8 |                       2.4 |
| 30_Generative Materials |                          17.6 |                             4.8 |                             10.7 |                                 4.3 |                         22   |                           28.3 |                           6.6 |                       5.7 |
| 45_Composite Laminates  |                          11   |                             0.3 |                             14.5 |                                 7.2 |                         29.7 |                           16.4 |                           7.3 |                      13.6 |
| 49_Alloy Thermodynamics |                           7.8 |                             1.7 |                             17.5 |                                 5   |                         31.8 |                           27.8 |                           4   |                       4.5 |
| 52_Polymer Chemistry    |                          12.3 |                             9   |                             12.4 |                                 3.7 |                         25.8 |                           23.3 |                           7.8 |                       5.7 |
| 8_Lithium Electrolytes  |                           4.3 |                            10   |                             14.7 |                                 8.8 |                         32.3 |                           18.3 |                           6.4 |                       5.2 |

## 4. Decoupling Volume and Efficiency (Impact Quadrants)
Classifies documents using median Journal IF and Citations Per Year (CPY). Shows which countries lead in high-utility efficiency vs pure volume.

| first_country   |   Coattail (High IF, Low CPY) |   Hidden Gem (Low IF, High CPY) |   Long Tail (Low IF, Low CPY) |   Star (High IF, High CPY) |   High-Utility Output (Star + Hidden Gem) % |
|:----------------|------------------------------:|--------------------------------:|------------------------------:|---------------------------:|--------------------------------------------:|
| United States   |                          15.2 |                            23.9 |                          23.5 |                       37.5 |                                        61.3 |
| United Kingdom  |                          18   |                            22.3 |                          21.3 |                       38.3 |                                        60.6 |
| Germany         |                          17   |                            23.4 |                          25.8 |                       33.9 |                                        57.2 |
| Canada          |                          15.7 |                            21.6 |                          29   |                       33.8 |                                        55.4 |
| South Korea     |                          25.8 |                            12.4 |                          21.1 |                       40.7 |                                        53.1 |
| China           |                          21.9 |                            14.9 |                          27.7 |                       35.6 |                                        50.5 |
| Italy           |                          21.1 |                            23.2 |                          30   |                       25.7 |                                        48.9 |
| France          |                          18.5 |                            20.6 |                          33.2 |                       27.6 |                                        48.3 |
| Turkey          |                          13.9 |                            22.2 |                          37.8 |                       26.1 |                                        48.2 |
| Spain           |                          23.7 |                            15.5 |                          30.1 |                       30.7 |                                        46.2 |
| India           |                          13.9 |                            21.8 |                          42.5 |                       21.9 |                                        43.7 |
| Japan           |                          18   |                            21.1 |                          38.3 |                       22.5 |                                        43.7 |
| Russia          |                          13.7 |                            24.1 |                          44.8 |                       17.4 |                                        41.5 |
| Iran            |                          18.5 |                            15.9 |                          44.2 |                       21.4 |                                        37.3 |
| Unknown         |                          23.4 |                            15.6 |                          43.8 |                       17.2 |                                        32.8 |

---

## 5. Automated Audits

### EVoC Sensitivity (reviewer #5)

Pairwise Adjusted Rand Index (ARI) between the EVoC layers computed in Step 6. ARI > 0.7 indicates stable clustering across resolutions; 0.3–0.7 moderate; < 0.3 sensitive (the layer choice materially changes the topic map).

| Layer pair | Topics (A → B) | ARI |
|---|---|---|
| Layer 3 vs Layer 4 | 60 → 14 | 0.292 |
| Layer 3 vs Layer 5 | 60 → 5 | 0.094 |
| Layer 4 vs Layer 5 | 14 → 5 | 0.367 |

### Regression Audit (reviewer #9)

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

### Growth Model Fitting (reviewer #11)

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

### Relevance Index Sensitivity (reviewer #10)

Skipped: no Relevance Index column is computed in this pipeline (RI is not standard in AKL). If RI is added later, this audit will verify the unit-invariance of the ranking.
