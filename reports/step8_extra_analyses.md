# Step 8 — extra analyses (questions 1-11)

Corpus: 36389 papers with a Step-6 topic, 2000-2025 (2026 excluded: partial year). Whole-field growth: 443 papers in 2015 -> 9136 in 2025 (x20.6). Because the whole field grows fast, topic dynamics are judged by **share of the yearly corpus**, not raw counts.

## A. Topic lifecycle and trajectory (Q1, Q11)
share* = % of the yearly corpus (3-year means). growth_yr_pct = log-linear fit of yearly counts 2015-2025 with a 95% interval for the slope (growth_lo/hi). Whole-field growth is ~35%/yr, so growth_yr_pct above that means gaining share. This is a trend description, not a forecast.

| topic                        |    n |   first_year_5p |   pre2010 |   share14_16 |   share17_19 |   share20_22 |   share23_25 |   growth_yr_pct |   growth_lo |   growth_hi | share_trend           |
|:-----------------------------|-----:|----------------:|----------:|-------------:|-------------:|-------------:|-------------:|----------------:|------------:|------------:|:----------------------|
| 45_Composite Laminates       | 1319 |            2001 |        63 |         4.17 |         3.08 |         3.44 |         3.62 |            37.4 |        31.5 |        43.6 | stable share          |
| 14_Molecular Descriptors     | 1305 |            2000 |       220 |         6.73 |         3.88 |         2.66 |         2.51 |            23.1 |        19.4 |        26.9 | declining share       |
| 21_Methane Catalysis         | 1136 |            2000 |       169 |         7.1  |         4.1  |         2.4  |         2.2  |            21   |        17.8 |        24.3 | declining share       |
| 16_Electrocatalysis          | 1129 |            2018 |         5 |         0.62 |         0.82 |         2.27 |         4.22 |            81   |        72.3 |        90.1 | rising share          |
| 29_Materials Prediction      | 1035 |            2016 |        11 |         1.49 |         3.31 |         3.45 |         3    |            45.3 |        33.2 |        58.5 | peaked, share falling |
| 30_Generative Materials      | 1028 |            2010 |        25 |         2.25 |         3.32 |         3.39 |         2.78 |            39.7 |        33.9 |        45.7 | peaked, share falling |
| 50_Atomistic Modeling        |  965 |            2011 |        13 |         1.61 |         2.69 |         2.82 |         2.9  |            41.5 |        37   |        46.2 | stable share          |
| 54_Atomistic Potentials      |  943 |            2005 |        14 |         1.87 |         3.67 |         3.09 |         2.58 |            35.7 |        30.5 |        41.2 | peaked, share falling |
| 43_Austenite Steel           |  941 |            2001 |       108 |         4.21 |         2.93 |         2.6  |         2.08 |            27.2 |        22.5 |        32   | declining share       |
| 26_Phonon Thermoelectricity  |  937 |            2012 |         2 |         1.51 |         2.39 |         2.56 |         2.97 |            48.1 |        42.7 |        53.7 | rising share          |
| 20_Nanoalloys                |  909 |            2000 |       179 |         9.05 |         5.1  |         2.19 |         0.93 |             3.9 |         2.3 |         5.5 | declining share       |
| 22_Catalysis                 |  891 |            2015 |        17 |         0.87 |         2.75 |         3.28 |         2.41 |            46.6 |        36.2 |        57.8 | peaked, share falling |
| 37_Magnesium Alloys          |  887 |            2004 |        66 |         2.49 |         1.85 |         2.08 |         2.48 |            38.9 |        32.9 |        45.1 | stable share          |
| 52_Polymer Chemistry         |  822 |            2006 |        29 |         1    |         1.35 |         2.22 |         2.57 |            57.3 |        48.4 |        66.7 | rising share          |
| 8_Lithium Electrolytes       |  781 |            2016 |         2 |         0.87 |         1.46 |         1.81 |         2.69 |            54.1 |        51.2 |        57.1 | rising share          |
| 55_Molecular Solvation       |  770 |            2001 |        32 |         2.83 |         2.65 |         2.31 |         2.03 |            29.6 |        24.4 |        35.1 | declining share       |
| 49_Alloy Thermodynamics      |  757 |            2018 |         3 |         0.29 |         0.75 |         2.07 |         2.63 |            76.5 |        66.6 |        87   | rising share          |
| 59_Molecular Synthesis       |  751 |            2006 |        27 |         0.75 |         2.21 |         2.51 |         2.11 |            50.2 |        30.4 |        73   | peaked, share falling |
| 18_Metasurfaces              |  729 |            2017 |         7 |         0.69 |         1.1  |         2.71 |         2.15 |            63.5 |        46.2 |        82.8 | peaked, share falling |
| 0_Photovoltaics              |  703 |            2009 |        23 |         0.81 |         1.69 |         1.88 |         2.08 |            48.2 |        35   |        62.7 | rising share          |
| 10_Nanoporous MOFs           |  690 |            2018 |         4 |         0.73 |         0.81 |         1.77 |         2.32 |            59.4 |        47.4 |        72.4 | rising share          |
| 11_Lithium Batteries         |  682 |            2017 |         2 |         0.28 |         0.89 |         1.6  |         2.35 |            65.7 |        59.3 |        72.4 | rising share          |
| 56_Molecular Prediction      |  664 |            2013 |        21 |         1.67 |         2.48 |         2.59 |         1.57 |            31.7 |        24   |        40   | peaked, share falling |
| 12_Battery Prediction        |  652 |            2011 |         8 |         1.83 |         1.18 |         1.45 |         2.05 |            42.1 |        35   |        49.6 | stable share          |
| 41_Superconductivity         |  643 |            2012 |        12 |         5.1  |         3.71 |         1.92 |         1.27 |            16.7 |        13.5 |        20   | declining share       |
| 28_Graphene Heterostructures |  637 |            2014 |         9 |         1.3  |         2.21 |         2.14 |         1.69 |            43.2 |        31.7 |        55.8 | peaked, share falling |
| 58_Catalytic Synthesis       |  618 |            2005 |        19 |         0.75 |         1.22 |         1.83 |         1.88 |            51.3 |        43.4 |        59.7 | stable share          |
| 32_Perovskite Lattice        |  605 |            2018 |         8 |         0.43 |         1.07 |         2.23 |         1.74 |            61   |        45.4 |        78.2 | peaked, share falling |
| 1_Chemical Sensing           |  599 |            2003 |        45 |         1.52 |         0.96 |         1.14 |         1.82 |            45   |        34.8 |        56   | stable share          |
| 4_Molecular Solvents         |  584 |            2007 |        24 |         3.42 |         2.3  |         1.49 |         1.4  |            25.7 |        22.4 |        29.1 | declining share       |
| 53_Nonadiabatic Reactions    |  582 |            2006 |        40 |         3.46 |         3.22 |         1.64 |         1.15 |            18.9 |        15   |        22.8 | declining share       |
| 42_Alloy Microstructure      |  563 |            2017 |         8 |         0.53 |         1.09 |         2.12 |         1.68 |            57.5 |        45   |        71   | peaked, share falling |
| 33_Molecular Solvation       |  517 |            2013 |        19 |         0.92 |         1.74 |         1.26 |         1.54 |            39.6 |        33.4 |        46.1 | rising share          |
| 57_Computational Chemistry   |  503 |            2016 |        11 |         0.56 |         1.49 |         1.75 |         1.42 |            49.8 |        35.9 |        65.2 | peaked, share falling |
| 51_Polymerization            |  491 |            2000 |       124 |         4.17 |         1.76 |         0.75 |         0.61 |             9.7 |         4.9 |        14.8 | declining share       |
| 6_Photocatalysis             |  488 |            2012 |        12 |         2.05 |         1.3  |         0.94 |         1.43 |            35.1 |        24.8 |        46.4 | declining share       |
| 19_Nanomaterials Synthesis   |  472 |            2014 |         4 |         0.91 |         1.27 |         1.74 |         1.22 |            44.4 |        36.7 |        52.6 | peaked, share falling |
| 25_Neuromorphic Memristors   |  469 |            2017 |         0 |         0.38 |         0.87 |         1.27 |         1.48 |            61.8 |        48.1 |        76.7 | rising share          |
| 24_Magnetic Materials        |  430 |            2005 |        20 |         0.58 |         1.43 |         1.23 |         1.22 |            43.4 |        35.4 |        52   | peaked, share falling |
| 47_Recrystallization         |  413 |            2007 |        42 |         2.97 |         2.01 |         1.02 |         0.72 |            18.4 |        13.5 |        23.5 | declining share       |
| 35_Alloy Solidification      |  395 |            2019 |         3 |         0    |         0.41 |         1.01 |         1.41 |            71.9 |        54.8 |        91   | rising share          |
| 48_Molecular Ligands         |  386 |            2012 |        16 |         0.89 |         0.89 |         1.27 |         0.98 |            39.8 |        31.3 |        48.9 | peaked, share falling |
| 38_Material Anisotropy       |  382 |            2012 |        20 |         0.47 |         0.72 |         1.15 |         1.15 |            58.2 |        43.7 |        74.2 | stable share          |
| 31_Perovskite Photovoltaics  |  377 |            2019 |         1 |         0.22 |         0.61 |         0.79 |         1.35 |            66.5 |        58   |        75.4 | rising share          |
| 44_Metamaterial Design       |  364 |            2016 |         6 |         0.79 |         0.59 |         0.87 |         1.17 |            45.2 |        35.8 |        55.2 | rising share          |
| 9_Zeolite Adsorption         |  362 |            2007 |        18 |         1.14 |         0.91 |         0.97 |         0.95 |            38.1 |        32.8 |        43.7 | stable share          |
| 2_Titanium Machining         |  358 |            2013 |        15 |         1.46 |         1.65 |         1.15 |         0.78 |            25.7 |        21   |        30.5 | declining share       |
| 13_Silicon Semiconductor     |  353 |            2018 |        16 |         0.23 |         0.79 |         0.91 |         1.07 |            54.7 |        43.9 |        66.3 | rising share          |
| 15_PEM Fuel Cells            |  331 |            2010 |        11 |         1.17 |         0.78 |         0.76 |         1    |            35.3 |        23.8 |        47.8 | stable share          |
| 34_Fiber Composites          |  324 |            2016 |         1 |         0.72 |         0.76 |         0.96 |         0.93 |            46   |        34.6 |        58.4 | stable share          |
| 39_Alloy Corrosion           |  321 |            2010 |        15 |         0.67 |         0.88 |         0.77 |         0.9  |            40.8 |        34.9 |        46.9 | rising share          |
| 27_Ferroelectric Perovskites |  307 |            2017 |         5 |         0.53 |         0.92 |         0.8  |         0.93 |            48.7 |        40   |        58   | rising share          |
| 40_Dielectric Polymers       |  297 |            2016 |         2 |         0.78 |         0.71 |         0.86 |         0.82 |            36.4 |        30.6 |        42.5 | stable share          |
| 3_Perovskite Oxides          |  294 |            2015 |         5 |         0.81 |         0.86 |         0.68 |         0.9  |            35   |        28.1 |        42.2 | stable share          |
| 46_Titanium Deformation      |  293 |            2006 |        28 |         2.53 |         0.85 |         0.52 |         0.58 |            20.1 |         8.9 |        32.3 | declining share       |
| 17_Wearable Sensing          |  284 |            2018 |         7 |         0.22 |         0.49 |         0.6  |         0.98 |            56.4 |        50.7 |        62.3 | rising share          |
| 7_MOF Adsorption             |  251 |            2016 |         4 |         0.94 |         1.18 |         0.66 |         0.63 |            28   |        20   |        36.5 | declining share       |
| 36_Friction Stir Welding     |  245 |            2013 |        12 |         0.95 |         0.62 |         0.72 |         0.66 |            31.8 |        23.9 |        40.2 | declining share       |
| 23_Alloy Microstructure      |  227 |            2018 |        11 |         0.16 |         0.73 |         0.47 |         0.71 |            50.2 |        38.2 |        63.2 | rising share          |
| 5_Polymer Membranes          |  198 |            2013 |         6 |         0.52 |         0.52 |         0.48 |         0.61 |            35.5 |        25.3 |        46.5 | stable share          |

**Top 5 gaining share:** 16_Electrocatalysis, 49_Alloy Thermodynamics, 11_Lithium Batteries, 8_Lithium Electrolytes, 10_Nanoporous MOFs

**Top 5 losing share:** 20_Nanoalloys, 21_Methane Catalysis, 14_Molecular Descriptors, 41_Superconductivity, 51_Polymerization

## B. Pioneers (Q2)
Share of early papers (<=2012) vs later papers by first-author country.

| country        |   total |   early_share |   recent_share |
|:---------------|--------:|--------------:|---------------:|
| China          |   11363 |          13.2 |           32.6 |
| United States  |    6307 |          10.1 |           17.9 |
| India          |    2056 |           5.4 |            5.7 |
| Germany        |    1545 |           4.4 |            4.2 |
| Japan          |    1504 |           2.9 |            4.2 |
| Iran           |    1155 |           9.9 |            2.7 |
| United Kingdom |    1138 |           4.6 |            3   |
| Unknown        |    1115 |          20.5 |            1.7 |
| South Korea    |    1085 |           1.8 |            3.1 |
| Canada         |     587 |           1.4 |            1.6 |
| France         |     483 |           1.8 |            1.3 |
| Switzerland    |     481 |           0.8 |            1.4 |

Topics with papers before 2011 (count): 14_Molecular Descriptors=254; 20_Nanoalloys=211; 21_Methane Catalysis=198; 51_Polymerization=139; 43_Austenite Steel=119; 45_Composite Laminates=78; 37_Magnesium Alloys=71; 47_Recrystallization=51; 53_Nonadiabatic Reactions=49; 1_Chemical Sensing=48; 46_Titanium Deformation=40; 52_Polymer Chemistry=35

## C. Application x method (Q3, Q10)
Counts (papers).

| app                                    |   Computational Design Methods |   Data-Driven Materials Science |   Deep Learning for Materials |   Evolutionary and Swarm Optimization |   Graph and Deep Neural Networks |   Hybrid Neural-Genetic Methods |   Machine Learning Interatomic Modeling |   Machine Learning Methods |   Machine Learning for Chemistry |   Neural Network Methods |   Recurrent Neural Networks |   Regression and Classification Methods |   Statistical Modeling & Analysis |   XGBoost and Ensemble Methods |
|:---------------------------------------|-------------------------------:|--------------------------------:|------------------------------:|--------------------------------------:|---------------------------------:|--------------------------------:|----------------------------------------:|---------------------------:|---------------------------------:|-------------------------:|----------------------------:|----------------------------------------:|----------------------------------:|-------------------------------:|
| Advanced Sensor Applications           |                             18 |                              11 |                            62 |                                    43 |                               51 |                               2 |                                       5 |                          4 |                              117 |                       87 |                           6 |                                       8 |                                14 |                              1 |
| Catalysis and Electrocatalysis         |                             48 |                              80 |                            51 |                                   204 |                               40 |                              22 |                                      53 |                         71 |                             1180 |                      294 |                           5 |                                     149 |                                66 |                             26 |
| Chemical Process Simulation            |                             29 |                              12 |                            47 |                                    59 |                               28 |                               6 |                                      10 |                         13 |                              179 |                      287 |                           8 |                                      16 |                                33 |                              1 |
| Chemical and Materials Research        |                             28 |                              61 |                            98 |                                    48 |                               25 |                               2 |                                      28 |                         16 |                              385 |                      165 |                          10 |                                      38 |                                32 |                              1 |
| Computational Structure Modeling       |                             57 |                              21 |                           110 |                                   425 |                               86 |                               6 |                                      85 |                         17 |                              423 |                      479 |                           7 |                                      33 |                                97 |                              8 |
| Energy and Thermal Systems             |                             17 |                              37 |                            33 |                                    86 |                               31 |                              22 |                                      35 |                         17 |                              285 |                      120 |                           8 |                                      16 |                                22 |                              2 |
| Environmental Separation and Treatment |                             21 |                              57 |                            44 |                                   131 |                               29 |                              27 |                                      20 |                         79 |                              370 |                      467 |                          15 |                                      72 |                                51 |                             14 |
| Material Analysis and Assessment       |                             32 |                              50 |                           149 |                                   186 |                              143 |                               6 |                                      53 |                         40 |                              411 |                      378 |                          19 |                                      71 |                                87 |                              8 |
| Material Property Prediction           |                            206 |                             179 |                           765 |                                  1320 |                              781 |                             143 |                                     395 |                        955 |                             3810 |                     3356 |                         162 |                                    1053 |                               671 |                            217 |
| Materials Data Analysis                |                             25 |                              24 |                           106 |                                    52 |                              112 |                               2 |                                       9 |                         28 |                              274 |                      136 |                          11 |                                      50 |                                36 |                              3 |
| Materials Design & Optimization        |                             82 |                              69 |                           279 |                                   181 |                              115 |                              19 |                                      32 |                         44 |                              512 |                      271 |                          18 |                                      69 |                                73 |                             17 |
| Materials Property Investigation       |                             72 |                              99 |                           185 |                                   178 |                               82 |                              23 |                                      68 |                         36 |                              786 |                      351 |                          18 |                                      73 |                                68 |                             11 |
| Materials for Chemical Applications    |                             20 |                              35 |                            32 |                                    45 |                               34 |                               9 |                                      27 |                         33 |                              308 |                      192 |                           6 |                                      40 |                                27 |                              7 |
| Phase and Microstructure Analysis      |                             16 |                               4 |                            45 |                                    76 |                               19 |                               4 |                                      33 |                          8 |                              185 |                      130 |                           3 |                                      16 |                                28 |                              2 |
| Process and Design Optimization        |                            204 |                             126 |                           114 |                                  1009 |                               74 |                             139 |                                      54 |                        181 |                              804 |                      957 |                          17 |                                     171 |                               176 |                             37 |

**Under-represented pairs (observed < 50% of expected, expected >= 30):** observed vs expected
- Computational Structure Modeling x Machine Learning Methods: 17 vs 83.7
- Computational Structure Modeling x Regression and Classification Methods: 33 vs 101.8
- Catalysis and Electrocatalysis x Deep Learning for Materials: 51 vs 142.1
- Catalysis and Electrocatalysis x Graph and Deep Neural Networks: 40 vs 110.6
- Process and Design Optimization x Graph and Deep Neural Networks: 74 vs 196.3
- Chemical and Materials Research x Machine Learning Methods: 16 vs 42.3
- Materials Property Investigation x Machine Learning Methods: 36 vs 92.5
- Chemical Process Simulation x Machine Learning Methods: 13 vs 32.9
- Energy and Thermal Systems x Regression and Classification Methods: 16 vs 40.1
- Chemical Process Simulation x Regression and Classification Methods: 16 vs 40.0
- Environmental Separation and Treatment x Graph and Deep Neural Networks: 29 vs 67.5
- Chemical and Materials Research x Evolutionary and Swarm Optimization: 48 vs 110.9

Method mix by year, % of papers (top 6 method categories), selected years.

|   year |   Machine Learning for Chemistry |   Neural Network Methods |   Evolutionary and Swarm Optimization |   Deep Learning for Materials |   Regression and Classification Methods |   Graph and Deep Neural Networks |
|-------:|---------------------------------:|-------------------------:|--------------------------------------:|------------------------------:|----------------------------------------:|---------------------------------:|
|   2005 |                              2.2 |                     48.1 |                                  33.9 |                           0   |                                     4.9 |                              0   |
|   2010 |                              3.1 |                     43.6 |                                  36.3 |                           0   |                                     4.6 |                              0   |
|   2015 |                              8.8 |                     29.8 |                                  36.1 |                           0.5 |                                     6.1 |                              0   |
|   2018 |                             19.4 |                     24.6 |                                  24.3 |                           3.8 |                                     5   |                              2.8 |
|   2020 |                             27.6 |                     22.8 |                                  12.7 |                           5.7 |                                     6   |                              5.6 |
|   2022 |                             30.9 |                     21.4 |                                   9.3 |                           7.5 |                                     4.9 |                              6.5 |
|   2024 |                             35.1 |                     19.4 |                                   5.9 |                           7.7 |                                     6   |                              5.5 |
|   2025 |                             37   |                     18   |                                   4.6 |                           7.6 |                                     5.2 |                              5   |

## D. Evidence vs volume (Q4, Q7)

| topic                        |   exp_validation_% |   no_or_cv_only_% |   dft_sim_data_% |   experimental_data_% |   named_benchmark_% |    n |   growth_yr_pct | share_trend           |
|:-----------------------------|-------------------:|------------------:|-----------------:|----------------------:|--------------------:|-----:|----------------:|:----------------------|
| 16_Electrocatalysis          |               30   |               5.5 |             77.2 |                  14.1 |                 4.3 | 1129 |            81   | rising share          |
| 49_Alloy Thermodynamics      |               54.2 |              13.5 |             43.6 |                  40.1 |                 8.1 |  757 |            76.5 | rising share          |
| 35_Alloy Solidification      |               70.6 |               9   |             11.3 |                  72.7 |                 3.5 |  395 |            71.9 | rising share          |
| 31_Perovskite Photovoltaics  |               48.5 |              11.7 |             38.4 |                  46.3 |                 7.4 |  377 |            66.5 | rising share          |
| 11_Lithium Batteries         |               46.8 |              11.8 |             41.1 |                  39.9 |                 7.2 |  682 |            65.7 | rising share          |
| 18_Metasurfaces              |               41.9 |               9.9 |             67.9 |                  25.2 |                 2.9 |  729 |            63.5 | peaked, share falling |
| 25_Neuromorphic Memristors   |               54.6 |               9.5 |             36.7 |                  50.4 |                17.1 |  469 |            61.8 | rising share          |
| 32_Perovskite Lattice        |               35.2 |              13.2 |             66   |                  22.2 |                 9.1 |  605 |            61   | peaked, share falling |
| 10_Nanoporous MOFs           |               28.7 |              10   |             68.7 |                  17   |                24.5 |  690 |            59.4 | rising share          |
| 38_Material Anisotropy       |               49.3 |               9.9 |             44.7 |                  48.3 |                 6   |  382 |            58.2 | stable share          |
| 42_Alloy Microstructure      |               47.8 |              18.7 |             30.6 |                  61.1 |                11.7 |  563 |            57.5 | peaked, share falling |
| 52_Polymer Chemistry         |               40.3 |              30.4 |             35.2 |                  47   |                10.6 |  822 |            57.3 | rising share          |
| 17_Wearable Sensing          |               77.6 |               9.3 |             19.3 |                  61.4 |                 1.1 |  284 |            56.4 | rising share          |
| 13_Silicon Semiconductor     |               52.4 |              16.9 |             33.2 |                  53.3 |                 5.7 |  353 |            54.7 | rising share          |
| 8_Lithium Electrolytes       |               36.1 |               5.2 |             76.4 |                  14.9 |                 5.5 |  781 |            54.1 | rising share          |
| 58_Catalytic Synthesis       |               40.5 |              26.6 |             30.8 |                  38.8 |                16.8 |  618 |            51.3 | stable share          |
| 59_Molecular Synthesis       |               21.3 |              40.6 |             27.1 |                  27.1 |                24.8 |  751 |            50.2 | peaked, share falling |
| 23_Alloy Microstructure      |               73.4 |               8.7 |              8.5 |                  82.4 |                 6.6 |  227 |            50.2 | rising share          |
| 57_Computational Chemistry   |               14.5 |               9.1 |             96.3 |                   2.8 |                15.5 |  503 |            49.8 | peaked, share falling |
| 27_Ferroelectric Perovskites |               41.4 |               6.4 |             69.3 |                  24.4 |                 5.9 |  307 |            48.7 | rising share          |
| 0_Photovoltaics              |               38.5 |              16.5 |             58.5 |                  25.1 |                10.5 |  703 |            48.2 | rising share          |
| 26_Phonon Thermoelectricity  |               27.2 |               4.2 |             88.1 |                   6.5 |                 6.7 |  937 |            48.1 | rising share          |
| 22_Catalysis                 |               25.4 |              11   |             77.1 |                  14   |                 6.5 |  891 |            46.6 | peaked, share falling |
| 34_Fiber Composites          |               57.9 |              21.9 |              6.3 |                  79.8 |                 6.2 |  324 |            46   | stable share          |
| 29_Materials Prediction      |               30.6 |              36.9 |             26.6 |                  31.2 |                10.7 | 1035 |            45.3 | peaked, share falling |
| 44_Metamaterial Design       |               43.4 |               5.4 |             75.8 |                  12.9 |                 4.9 |  364 |            45.2 | rising share          |
| 1_Chemical Sensing           |               49   |              15   |             50.1 |                  42.6 |                 3   |  599 |            45   | stable share          |
| 19_Nanomaterials Synthesis   |               53.6 |              21.2 |             24   |                  57.2 |                 4.9 |  472 |            44.4 | peaked, share falling |
| 24_Magnetic Materials        |               41.9 |               9.7 |             58.3 |                  28.6 |                10.7 |  430 |            43.4 | peaked, share falling |
| 28_Graphene Heterostructures |               21.9 |               5.4 |             85   |                  10.9 |                12.4 |  637 |            43.2 | peaked, share falling |
| 12_Battery Prediction        |               58.5 |              13.3 |              9.5 |                  79   |                25.6 |  652 |            42.1 | stable share          |
| 50_Atomistic Modeling        |               29.6 |               4.3 |             90.9 |                   6.7 |                 5.6 |  965 |            41.5 | stable share          |
| 39_Alloy Corrosion           |               65.7 |              14.3 |             14.1 |                  75.6 |                 7.2 |  321 |            40.8 | rising share          |
| 48_Molecular Ligands         |               29.1 |              17.9 |             79.2 |                  14.6 |                17.6 |  386 |            39.8 | peaked, share falling |
| 30_Generative Materials      |               28.2 |              16.4 |             66.7 |                  16.5 |                29.5 | 1028 |            39.7 | peaked, share falling |
| 33_Molecular Solvation       |               29   |               2.2 |             92.4 |                   5   |                 3.1 |  517 |            39.6 | rising share          |
| 37_Magnesium Alloys          |               69.2 |              14.1 |             11.3 |                  77.6 |                 3.9 |  887 |            38.9 | stable share          |
| 9_Zeolite Adsorption         |               43.4 |              11.3 |             43.6 |                  41.5 |                12.7 |  362 |            38.1 | stable share          |
| 45_Composite Laminates       |               61.8 |              13.2 |             21.9 |                  70.7 |                 5.7 | 1319 |            37.4 | stable share          |
| 40_Dielectric Polymers       |               58.9 |              10.5 |             36.7 |                  51.8 |                 5.4 |  297 |            36.4 | stable share          |
| 54_Atomistic Potentials      |               24   |               9   |             95.5 |                   2.5 |                14.6 |  943 |            35.7 | peaked, share falling |
| 5_Polymer Membranes          |               44.8 |              16.9 |             34.2 |                  47.7 |                 6.1 |  198 |            35.5 | stable share          |
| 15_PEM Fuel Cells            |               42.9 |              14.5 |             23.9 |                  63.7 |                 4.8 |  331 |            35.3 | stable share          |
| 6_Photocatalysis             |               64   |              11.2 |             19.6 |                  69.8 |                 3.9 |  488 |            35.1 | declining share       |
| 3_Perovskite Oxides          |               47.5 |               5   |             62.5 |                  30.3 |                 2.7 |  294 |            35   | stable share          |
| 36_Friction Stir Welding     |               76.4 |               7.6 |              7.3 |                  88   |                 2.4 |  245 |            31.8 | declining share       |
| 56_Molecular Prediction      |               15.3 |              16.7 |             91.1 |                   5.6 |                26.5 |  664 |            31.7 | peaked, share falling |
| 55_Molecular Solvation       |               29.9 |              11.4 |             89   |                   7.5 |                17   |  770 |            29.6 | declining share       |
| 7_MOF Adsorption             |               69.5 |               8.6 |             18.9 |                  67   |                 2.4 |  251 |            28   | declining share       |
| 43_Austenite Steel           |               55.6 |              15.9 |             12.8 |                  64.1 |                 6.3 |  941 |            27.2 | declining share       |
| 2_Titanium Machining         |               80.2 |               3.7 |              4.1 |                  93.1 |                 3.1 |  358 |            25.7 | declining share       |
| 4_Molecular Solvents         |               46.5 |              18.1 |             28.2 |                  56.9 |                 6   |  584 |            25.7 | declining share       |
| 14_Molecular Descriptors     |               30   |              38.6 |             27.6 |                  52.5 |                12   | 1305 |            23.1 | declining share       |
| 21_Methane Catalysis         |               54.6 |              10.3 |             13.1 |                  70.6 |                 5.1 | 1136 |            21   | declining share       |
| 46_Titanium Deformation      |               79.7 |               6.3 |              6.6 |                  85.5 |                 1.4 |  293 |            20.1 | declining share       |
| 53_Nonadiabatic Reactions    |               36.7 |               2   |             96.6 |                   2.5 |                 6.5 |  582 |            18.9 | declining share       |
| 47_Recrystallization         |               80.4 |               4.8 |              1.4 |                  96.4 |                 1.5 |  413 |            18.4 | declining share       |
| 41_Superconductivity         |               24.4 |               4.4 |             90.3 |                   5.1 |                 8.2 |  643 |            16.7 | declining share       |
| 51_Polymerization            |               40.8 |              15.6 |             12.8 |                  60.3 |                 5.9 |  491 |             9.7 | declining share       |
| 20_Nanoalloys                |               18.7 |               2.9 |             97.4 |                   1.8 |                 3.3 |  909 |             3.9 | declining share       |

Spearman(growth rate, experimental-validation share) across topics: rho=-0.04, p=0.742

Median citations/year by topic: 16_Electrocatalysis=10.0; 17_Wearable Sensing=10.0; 10_Nanoporous MOFs=8.26; 11_Lithium Batteries=7.88; 49_Alloy Thermodynamics=7.8; 12_Battery Prediction=7.53; 1_Chemical Sensing=7.5; 25_Neuromorphic Memristors=7.5; 8_Lithium Electrolytes=7.0; 35_Alloy Solidification=7.0; 44_Metamaterial Design=6.5; 31_Perovskite Photovoltaics=6.33; 6_Photocatalysis=6.22; 7_MOF Adsorption=6.0; 32_Perovskite Lattice=5.83; 15_PEM Fuel Cells=5.67; 18_Metasurfaces=5.6; 23_Alloy Microstructure=5.5; 54_Atomistic Potentials=5.33; 29_Materials Prediction=5.0; 52_Polymer Chemistry=5.0; 59_Molecular Synthesis=5.0; 57_Computational Chemistry=5.0; 58_Catalytic Synthesis=5.0; 40_Dielectric Polymers=5.0; 22_Catalysis=5.0; 19_Nanomaterials Synthesis=5.0; 34_Fiber Composites=4.71; 30_Generative Materials=4.67; 26_Phonon Thermoelectricity=4.67; 5_Polymer Membranes=4.67; 0_Photovoltaics=4.67; 56_Molecular Prediction=4.25; 9_Zeolite Adsorption=4.22; 3_Perovskite Oxides=4.19; 4_Molecular Solvents=4.0; 27_Ferroelectric Perovskites=4.0; 55_Molecular Solvation=4.0; 33_Molecular Solvation=4.0; 48_Molecular Ligands=4.0; 50_Atomistic Modeling=4.0; 42_Alloy Microstructure=3.83; 45_Composite Laminates=3.8; 39_Alloy Corrosion=3.67; 36_Friction Stir Welding=3.5; 38_Material Anisotropy=3.45; 28_Graphene Heterostructures=3.4; 47_Recrystallization=3.27; 37_Magnesium Alloys=3.25; 46_Titanium Deformation=3.06; 2_Titanium Machining=3.0; 24_Magnetic Materials=3.0; 13_Silicon Semiconductor=3.0; 21_Methane Catalysis=2.64; 43_Austenite Steel=2.62; 53_Nonadiabatic Reactions=2.57; 14_Molecular Descriptors=2.25; 41_Superconductivity=2.2; 20_Nanoalloys=1.75; 51_Polymerization=1.44

## E. Future directions (Q9)
Share of direction mentions by macro-category, recent vs earlier.

| macro_category                    |   total |   share_2023_25_% |   share_2015_20_% |   ratio |
|:----------------------------------|--------:|------------------:|------------------:|--------:|
| Future Research Directions        |    5458 |             26.19 |             22.63 |    1.16 |
| Materials Design & Discovery      |    2807 |             13.06 |             14    |    0.93 |
| Computational Materials Design    |    2111 |              9.71 |              9    |    1.08 |
| Computational Catalyst Design     |    1477 |              7.07 |              6.85 |    1.03 |
| AI-Driven Materials Science       |    1457 |              6.7  |              6.68 |    1    |
| Optimization Strategies           |    1229 |              5.42 |              6.02 |    0.9  |
| Application Expansion & Future    |    1202 |              5.38 |              6.55 |    0.82 |
| Methodological Advancements       |    1179 |              5.49 |              5.63 |    0.98 |
| Computational Multiscale Modeling |    1161 |              5.1  |              5.76 |    0.89 |
| Data-Driven Materials Discovery   |    1082 |              4.38 |              6.65 |    0.66 |
| Advanced Device Technologies      |     907 |              4.52 |              3.61 |    1.25 |
| Machine Learning in Chemistry     |     799 |              3.87 |              3.41 |    1.13 |
| Autonomous Scientific Systems     |     424 |              2.02 |              1.95 |    1.04 |
| AI in Chemistry                   |     249 |              1.1  |              1.26 |    0.87 |

Share (%) of papers whose extracted direction labels match each theme:

| theme                           |   mentions |   2015 |   2018 |   2020 |   2022 |   2024 |   2025 |
|:--------------------------------|-----------:|-------:|-------:|-------:|-------:|-------:|-------:|
| LLM / language models           |         24 |    0   |    0   |    0   |    0   |    0.3 |    0.4 |
| autonomous / self-driving lab   |        169 |    0   |    1.3 |    0.6 |    1.1 |    0.7 |    1.4 |
| inverse design / generative     |        234 |    1.1 |    1   |    1.7 |    1.9 |    1.2 |    1.5 |
| transfer learning / foundation  |         73 |    0   |    0   |    0.1 |    0.5 |    0.5 |    0.6 |
| interpretability / explainable  |         36 |    0   |    0   |    0   |    0.2 |    0.5 |    0.3 |
| uncertainty quantification      |          8 |    0   |    0   |    0.2 |    0.1 |    0.1 |    0   |
| active learning / Bayesian opt. |         70 |    0   |    0   |    0.6 |    1   |    0.4 |    0.4 |
| physics-informed / hybrid       |        130 |    0   |    0.6 |    0.4 |    0.6 |    0.6 |    1.5 |
| multi-scale / multimodal        |        147 |    0   |    1.6 |    1   |    0.7 |    0.8 |    1.4 |
| data / benchmarks               |        178 |    1.1 |    0.6 |    1.2 |    1.6 |    1.2 |    1.2 |

Top domain challenges overall: Challenging Application Contexts (3503); Project Costs and Resources (3406); Process and Materials Challenges (2705); Synthesis and Scale-Up (2577); Industrial Translation (2446); Practical Applications & Design (2398); Experimental and Modeling Complexities (2390); Experimental and Stability Challenges (2302)
