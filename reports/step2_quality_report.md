# AKL Step 2 — Data Quality Report

Generated: 2026-11-02 16:54:06

## Summary

| Metric | Value |
|--------|-------|
| Records input (Step 1) | 61403 |
| Removed — missing mandatory fields | 2491 |
| Removed — abstract too short (<50 chars) | 9 |
| Removed — outside analysis window (2000–2026) | 363 |
| Removed — language filter (English) | 57 |
| Removed — duplicates (DOI + title) | 482 |
| Removed — missing extra required fields | 1 |
| **Records output (corpus_clean)** | **58000** |
| Retention rate | 94.5% |

## Mandatory fields checked

- `title`
- `abstract`
- `year`
- `first_author`
- `last_author`

## Language handling

- Language detection: **enabled** (langdetect on title + abstract; on divergence, the abstract language is used).
- Language filter: keep only records with language = **English**.

## Extra required fields checked

- `doi`

## Analysis window

- Corpus restricted to publication years **2000–2026** (inclusive).
- Records outside this window (e.g. early-access items dated after the window end) were removed.