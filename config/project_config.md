# Project Configuration — AKL Pipeline

> This file is read by the orchestrator agent at the beginning of each session.
> Fill in the sections marked with `[FILL]` before starting the pipeline.
> Sections marked with `[OPTIONAL]` can be left blank — the pipeline will use default values.
> Do not remove empty sections: they may be necessary in future steps.

---

## 1. Project identification

- **Project name:** "ML_ripe_hype"
- **Creation date:** "2026-11-02"
- **Responsible:** Ronaldo Cristiano Prati and Luis Cesar de Azevedo
- **Advisor:** [OPTIONAL]
- **Institution:** [OPTIONAL]

---

## 2. Research objective

> This study assesses whether machine learning (ML) in chemistry and materials science is a mature field or still largely hype. Using a bibliometric and semantic mapping of the literature from 2000 onward, it traces how ML was adopted across chemistry and materials subfields (from early adopters to recent entrants), how the dominant methods evolved, which benchmarks and best practices have emerged, and what the key findings and outcomes of the field have been. Application areas are classified by signs of maturity (growth plateau, experimental validation, consolidated methods, benchmarks and best practices, real-world deployment) versus signs of hype (rapid growth driven by method demonstrations, computational-only claims, limited validation or reproducibility). The scope covers ML/AI as a research instrument for chemistry and materials problems (property prediction, materials discovery, reaction and synthesis planning, simulation and force fields, spectroscopy and characterization). It excludes general ML methodology papers without a chemistry or materials application, and drug discovery or biomedical applications.

---

## 3. Domain and thematic area

- **Main area:** chemistry and materials science
- **Relevant subareas:** machine learning / artificial intelligence; computational chemistry; cheminformatics; materials informatics; molecular and materials simulation (DFT, molecular dynamics, force fields); reaction prediction and synthesis planning; spectroscopy and characterization; catalysis; energy materials
- **Period of interest:** "2000–2025" (2026 treated as a partial year; early adopters from 2000)
- **Corpus languages:** "English"

---

## 4. Research questions

1. **Early adopters:** Which chemistry and materials subfields adopted ML first, and when did each take off since 2000?
2. **Maturity vs. hype:** Which application areas show a growth plateau and consolidation (mature), and which are still growing exponentially (hype candidates)?
3. **Methods:** Which ML methods dominate (classical methods, neural networks, graph neural networks, generative models, foundation models and LLMs), and how has the method mix evolved over time?
4. **Benchmarks:** Which benchmarks and datasets are established in each subfield, and which areas still lack standard benchmarks for comparing methods?
5. **Best practices:** What best practices are reported or recommended (data curation, validation protocols, uncertainty quantification, reproducibility, reporting standards), and how widely are they adopted?
6. **Key findings and outcomes:** What are the main findings and demonstrated outcomes (e.g., experimentally validated discoveries, accuracy gains over conventional methods, deployed tools), and in which subfields do they concentrate?
7. **Validation:** How often are results validated experimentally rather than only computationally, and does this vary by subfield?
8. **Bottlenecks:** What are the most reported challenges (data scarcity and quality, reproducibility, transferability and extrapolation, interpretability), and in which topics do they weigh most?
9. **Geography:** Which countries and institutions lead, and who are the pioneers versus recent entrants?
10. **Hype signals:** Where do publication volume and citations grow faster than evidence of validation, benchmarks and real-world use?
11. **Applications:** Which chemistry and materials problems concentrate the most work, and which are mature versus still emerging?
12. **Application-method pairs:** Which application-method combinations dominate, and where are cross-overs missing?
13. **Readiness:** In which applications is there real laboratory or industrial use, and in which only proof of concept?
14. **Domain challenges:** Which domain-specific difficulties (synthesis, scale-up, experimental data) limit each application, beyond ML challenges?

---

## 5. Data source (Step 1)

- **Chosen source:** WOS (upload) + OpenAlex (query) — combined acquisition. arXiv is NOT used in this project (see below)
- **Upload filename:** "data_wos.txt" (placed in `data/01_raw/`; 11 Fast 5000 exports merged, 52,035 records, query run on 2026-11-02)
- **Search query (WOS, Advanced Search):**
  ```
  TS=("machine learning" OR "deep learning" OR "neural network*" OR "artificial intelligence"
      OR "random forest*" OR "graph neural network*" OR "support vector" OR "generative model*"
      OR "data-driven"
      OR "evolutionary algorithm*" OR "evolutionary computation" OR "genetic algorithm*"
      OR "genetic programming" OR "particle swarm" OR "differential evolution"
      OR "swarm intelligence" OR "evolutionary optimi*")
  AND
  TS=("materials science" OR "materials discovery" OR "materials informatics" OR cheminformatics
      OR chemoinformatics OR "computational chemistry" OR "property prediction"
      OR "interatomic potential*" OR "force field*" OR retrosynthesis OR "reaction prediction"
      OR catalys* OR "density functional"
      OR "materials design" OR "materials genome" OR "inverse design"
      OR "crystal structure prediction" OR "high-throughput screening"
      OR "self-driving lab*" OR "autonomous experiment*"
      OR "molecular dynamics" OR "quantum chemistry" OR "ab initio"
      OR "machine learning potential*" OR "neural network potential*" OR "band gap"
      OR "synthesis planning" OR retrosynthetic OR "reaction outcome*" OR "reaction optimi*"
      OR "organic synthesis"
      OR perovskite* OR "metal-organic framework*" OR zeolite* OR polymer* OR alloy*
      OR battery OR batteries OR electrolyte*
      OR "chemical space" OR "molecular representation*" OR "molecular descriptor*"
      OR SMILES OR "quantitative structure-property" OR QSPR)
  AND WC=("Chemistry*" OR "Materials Science*" OR "Physics, Condensed Matter" OR "Physics, Applied"
          OR "Engineering, Chemical" OR "Nanoscience & Nanotechnology")
  AND PY=(2000-2026) AND DT=(Article OR Review) AND LA=English
  NOT TS=("drug discovery" OR "drug design" OR "drug development" OR "virtual screening"
          OR QSAR OR "quantitative structure-activity")
  ```
  Result: 52,035 records. The Fast 5000 export carries no Author Keywords, Language, Author Full Names or ISSN; citations come from `TC` (Core Collection).
- **Search query (OpenAlex):** `primary_topic.id:T11948` ("Machine Learning in Materials Science") AND title_and_abstract.search:("machine learning" OR "deep learning" OR "neural network" OR "neural networks" OR "artificial intelligence" OR "random forest" OR "genetic algorithm" OR "evolutionary algorithm" OR "graph neural network" OR "generative model" OR "support vector") — ~20,800 works estimated on 2026-11-02 (topics are model-assigned and may change)
- **OpenAlex filters:** type:article|review; language:en; has_doi:true; from_publication_date:2000-01-01; to_publication_date:2026-12-31
- **arXiv:** not used. ~8,500 preprints matched ML terms in cond-mat.mtrl-sci or physics.chem-ph (2026-11-02), but they mostly duplicate published work, carry no citations or reliable affiliations, and would inflate a corpus already above 50,000 records. Can be added later with `workers/step1_worker.py arxiv` and merged by DOI.
- **PubMed API key:** [NOT USED]
- **Filters applied at the source:** "document type: Article or Review; language: English; drug discovery and QSAR excluded (WOS)"
- **Max results to fetch:** 50000
- **Estimated total records:** WOS 52,035 + OpenAlex ~20,800 (before dedup); the overlap is not yet measured, expected total after dedup by DOI ~55,000–65,000
- **Merge strategy:** concatenate + dedup by DOI (priority: WOS → OpenAlex); `publication_date` preserved for month-level filtering
- **Analysis window:** 2000–2026 (early adopters from 2000); 2026 treated as a partial year in trend analyses (data through ~Nov 2026); 2027 early-access records (present in the WOS export) excluded

> **Note for Generic CSV users:** After placing your CSV in `data/01_raw/`, edit the `source_mapping.generic` section in `pipeline_config.yaml` to map your CSV column names to the AKL canonical schema. See `generic_csv_import_guide.md` for detailed instructions.

---

## 6. Relevance criteria (Step 4)

> Describe what makes a document relevant to this study.
> The agent will use these criteria to suggest the classification of the sample.

### RELEVANT document when:
- Applies machine learning or AI (including evolutionary computation, e.g., genetic algorithms) as a method to solve a chemistry or materials science problem: property prediction, molecule or materials discovery and design, reaction and synthesis planning, ML potentials and force fields, spectroscopy and characterization analysis, catalysis, energy materials.
- Reviews, perspectives, benchmarks, datasets, or discussions of best practices, reproducibility, validation, limitations or hype in ML for chemistry and materials.
- Reports validation (experimental or computational) of ML predictions, or deployment of ML-driven workflows (e.g., self-driving labs).
- Early-era work counts too: "artificial neural networks", "genetic algorithms" and QSPR-style models in chemistry or materials (2000s).

### NOT RELEVANT document when:
- Focuses on drug discovery, QSAR for biological activity, or clinical/biomedical applications.
- Is an ML methodology paper where chemistry or materials data is only one of many benchmark datasets, with no chemistry or materials contribution.
- Mentions ML only in passing (e.g., one line of future work) while the paper's contribution is non-ML.
- Concerns industrial process control or monitoring with neural networks, or civil/structural engineering (e.g., concrete strength prediction), without chemistry or materials insight.
- Uses "neural network" in the biological sense, or "data-driven" without machine learning.

### Examples of relevant titles (optional but recommended):
- "Neural network potentials for reactive molecular dynamics"
- "Machine learning-guided discovery of perovskite photovoltaic materials with experimental validation"
- "Genetic algorithm structure prediction for atomic clusters"
- "Best practices for machine learning in materials property prediction"

### Examples of not relevant titles (optional but recommended):
- "Machine learning for virtual screening of kinase inhibitors"
- "Neural network control of a continuous stirred-tank reactor"
- "Prediction of concrete compressive strength using artificial neural networks"


---

## 7. Semantic extraction vectors (Step 7)

> Define which semantic dimensions should be extracted from the texts.
> The 'Scope' indicates if the extraction happens sentence by sentence (more granular) or scanning the entire abstract (for unique overall identifiers).
> Leave the "Active" field as "yes" or "no" to control which ones will be executed.

| Vector | Description | Scope | Active |
|---|---|---|---|
| challenges | ML and data challenges, limitations or open problems (e.g., data scarcity, reproducibility, transferability, interpretability) | sentence | yes |
| best_practices | Recommended practices or guidelines (data curation, validation protocol, uncertainty quantification, reporting standards) | sentence | yes |
| ml_methods | Main ML or AI method family used (e.g., graph neural network, random forest, genetic algorithm, large language model) | abstract | yes |
| validation | How the reported results are validated. Use exactly one of: experimental validation (new measurements or synthesis confirm predictions), computational benchmark (compared with DFT, simulation or other methods), cross-validation only (held-out data splits), no validation. Answer None if the text does not say | abstract | yes |
| findings | Main concrete result stated (e.g., a new material or catalyst identified, a quantified speed-up or error reduction, a negative result). Be specific, not generic like 'accuracy gain'. Answer None if no concrete result is stated | abstract | yes |
| benchmarks_datasets | Named benchmark or dataset used (e.g., Materials Project, QM9) | abstract | yes |
| application_task | Chemistry or materials problem addressed (e.g., property prediction, catalyst discovery, synthesis optimization, process control, spectra and characterization, force fields) | abstract | yes |
| material_system | Material class or chemical system studied (e.g., MOFs, alloys, polymers, perovskites, batteries, heterogeneous catalysts) | abstract | yes |
| target_property | Specific property or outcome predicted or optimized (e.g., band gap, reaction yield, ionic conductivity). Answer None if none is named | abstract | yes |
| data_source | Where the training data comes from. Use exactly one of: DFT or simulation, experiments, literature text mining, public database, industrial data, mixed. Answer None if the text does not say | abstract | yes |
| application_challenges | Domain challenges, not ML ones (e.g., synthesis cost, lab-to-industry scale-up, noisy measurements, real operating conditions) | sentence | yes |
| readiness | Evidence of real-world use beyond a proof of concept, ONLY if explicitly stated. Use exactly one of: laboratory use (integrated in a lab workflow, autonomous or self-driving lab, predictions routinely used by experimentalists), industrial or deployed (used in production, released software tool or platform). Answer None for ordinary research studies, including those validated experimentally (that is captured by the validation vector) | abstract | no |
| directions | Future research directions (methods or applications) | sentence | yes |
| controversies | Controversies or disagreements between authors | sentence | no |

**Specific domain instruction for materials extraction:** Focus on machine learning or AI applied to chemistry and materials science. Extract both the ML method and the application side (problem, material system, property, domain challenges, readiness); ignore generic ML methodology.

---

## 8. Questions and Instructions for Step 8 (Specialized Synthesis)

> The Agent will automatically generate a Deep Scientometric Analysis containing:  
> 1. Thematic Lifecycle (Exponential vs Plateau topics)  
> 2. Strategic Geopolitics (Pioneers vs Traditionalists)  
> 3. Bottleneck Regimes (Row-normalized Challenges by Topic)  
> 4. Impact Quadrants (Volume vs Efficiency)  
>
> List below any additional specific questions the agent should answer based on the data.

**Analytical Questions & Focus Areas:**
1. **Maturity by topic:** Classify each of the 46 topics (Step 6, layer 3) as emerging, exponential or plateau using the yearly publication series since 2000. List the 5 most mature and the 5 fastest-growing topics, and say whether recent growth outpaces citation growth (hype signal).
2. **Pioneers and early adopters:** Which topics already had publications before 2010? Which countries and institutions lead the early topics, and which entered later?
3. **Application x method:** Which `application_task` x `ml_methods` pairs dominate, and which plausible combinations are rare? Show how the method mix (classical, neural networks, GNNs, generative models, LLMs) evolved over time.
4. **Evidence vs. volume (hype):** For each topic, compare publication volume with the share of papers that have experimental validation (`validation`), a named benchmark (`benchmarks_datasets`) and a concrete result (`findings`). Which topics grow faster than their evidence?
5. **Bottlenecks by topic:** Using row-normalized counts, which ML and data challenges (`challenges`) and which domain challenges (`application_challenges`) weigh most in each topic, and how do the two differ?
6. **Best practices:** Which practices (`best_practices`) are cited most, and in which topics are they rarely mentioned?
7. **Data source and benchmarks:** What is the share of DFT/simulation versus experimental data (`data_source`) per topic, and which topics lack a standard benchmark?
8. **Verdict by area:** For each main area give (a) the current state (mature, promising, probable hype) with supporting data and (b) the outlook: what is still missing to mature (experimental validation, benchmarks, data, best practices).
9. **What authors point to next:** Which future directions (`directions`) are most cited per topic and per year? Which are recurrent (e.g., inverse design, transfer learning, autonomous labs, LLMs) and which appear only in the last 2-3 years? Treat them as a signal, not as evidence: authors' statements tend to repeat generic claims ("more data", "future work").
10. **White spaces:** Which application x method (or application x material) combinations are plausible but have very few papers, and are suggested as opportunities by `directions` or by the bottlenecks? List the 10 most promising.
11. **Likely trajectory:** Using the yearly series 2000-2025 (2026 is partial: exclude it from fits), indicate for each topic whether the trend is accelerating, plateauing or declining, and which topics have the highest recent growth. State explicitly that this is an extrapolation, not a forecast, and report the uncertainty.

**Cautions for the agent:**
- The `readiness` vector was discarded (it confused experimental validation with laboratory use): do not use it. Read maturity through `validation` instead.
- The Step 5 filter has a noisy boundary (P(yes) between 0.40 and 0.60): keep the boundary audit enabled and report its precision.
- Topics refer to the final Step 6 layer (layer 3, 46 topics). EVoC layers are not reproducible across runs, so do not compare with other layers.

---

## 9. Expected visualizations (Step 9)

> Indicate which visualizations are a priority for the final report.
> The standard set will always be generated. List additional desired visualizations here.

**Standard set (always generated):**
- Topographic topic map
- Temporal evolution of clusters
- Distribution of publications per year
- Word cloud per cluster
- Term co-occurrence network

**Additional requested visualizations:**
- Heatmap of application x method (paper counts), highlighting low-count white spaces
- Stacked area chart of the method mix per year (classical, neural networks, GNNs, generative models, LLMs)
- Emerging future directions per year (top `directions` categories, last 5 years vs. before)
- Evidence vs. volume scatter per topic (validation share against publication growth)
- Further priority-A and priority-B figures (topic share over time, lifecycle map, bottleneck heatmaps, data source by topic, pioneers and geography, growth-rate forest plot, audit transparency) are specified in `data/04_reports/step8_visualizations_requested.md`

---

## 10. Notes and free observations

> Space for the expert to record decisions, additional context, or relevant observations
> that do not fit in the sections above. The agent reads this section
> but does not process it in a structured way — it serves as context memory.

[OPTIONAL]

---

## Essential data fields

The following fields are required for every record: doi.

---

## 11. Pipeline configuration overrides

> Describe in natural language any pipeline configuration adjustments you want to apply.
> The automation will translate these requests into `pipeline_config.yaml` values.
> To see all available options, open `pipeline_config.yaml` — it contains the technical
> defaults for every step. You only need to write here what you want to change.
> Examples: "audit 100 challenge sentences", "use the gemma-3-4b model via vLLM",
> "increase batch_size to 32".

[OPTIONAL — no overrides requested yet]

---

## Change history

| Date | Changed section | Description |
|---|---|---|
| 2026-09-14 | All | Initial file creation |
| 2026-09-14 | 5 | Switched from PubMed to combined WOS + OpenAlex acquisition (variant D: title+abstract, type:article, 2016-08-01 → 2026-08-31) |
| 2026-09-15 | 5 | Added arXiv API acquisition (variant C: all: + categories cs.SE/CY/HC/PL/AI, 186 results); DataCite fallback DOI `10.48550/arXiv.<id>` for preprints without published DOI; merge priority WOS → OpenAlex → arXiv |
| 2026-09-15 | 5 | Pre-Step-2 enrichment (`workers/step1_language_if_worker.py`): language column validated/corrected via langdetect (102 corrections; 3 Korean, 14 other→English, 85 empty/Ang→English); missing `journal_if` filled via impact_factor + OpenAlex 2yr_mean_citedness (121 filled; 612/924 total); `jnif` recomputed |
| 2026-09-16 | 5 | Analysis window set to **2023–2026** (Option A, specialist-confirmed): pre-2023 records (12, mostly tangential to GenAI education) and 2027 early-access records (3) excluded; 2026 flagged as partial year in trends |
| 2026-10-06 | 11 | Added Section 11 "Pipeline configuration overrides": natural-language interface for adjusting `pipeline_config.yaml` values at session start |
| 2026-11-02 | 6, 7 | Relevance criteria rewritten for ML in chemistry and materials (drug discovery, process-control ANNs and generic ML methodology excluded). Step 7 vectors: challenges, best_practices (sentence); ml_methods, validation, findings, benchmarks_datasets (abstract); directions and controversies inactive |
| 2026-11-02 | 5 | Data sources: WOS query (52,035 records, Fast 5000 export) + OpenAlex (topic T11948 + ML terms); arXiv left out; analysis window 2000–2026. `pipeline_config.yaml` updated (OpenAlex filters, Step 2 years) |
| 2026-11-02 | 1, 2, 3, 4, 5 | New project "ML_ripe_hype" (ML in chemistry and materials science: ripe or hype). Rewrote identification, objective, domain, period (2000–2025, 2026 partial) and research questions; drug discovery excluded; `max_results` raised to 50000. Sections 5–9 still describe the previous project and must be rewritten |
| 2026-11-03 | 7, 8, 9 | Step 7 vectors expanded to applications (application_task, material_system, target_property, data_source, application_challenges); readiness discarded; Section 8 questions 1-11 (incl. future-oriented 9-11) and Section 9 extra visualizations filled
