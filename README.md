# PISA 2025: Mongolia vs. Rwanda

What factors may explain differences in PISA performance between **Mongolia** and **Rwanda**?
Final project for 90-819 Python Programming II (Carnegie Mellon University), by **Brian Adjetey**
and **Anar**.

> **Status: scaffold.** The repository is intentionally near-empty at this stage. The extraction
> script, the derived analysis table, and the analysis notebook land here as the project is built.

## Data

All data comes from the **OECD Programme for International Student Assessment (PISA), 2025 cycle**
(the ninth cycle — hence the `CY09` filename prefix; `MS` = main study, `PUF` = public use file).
Both countries participated in 2025: Rwanda for the first time, Mongolia as a partner country.

| What | Where |
|---|---|
| Original source | [OECD PISA 2025 Database](https://www.oecd.org/en/data/datasets/pisa-2025-database.html) |
| The two raw files we use, zipped | [Google Drive folder](https://drive.google.com/drive/folders/1Me0GPML6cYotrSabFRuJkklFSHpzSk8F?usp=drive_link) |

**The raw data is not stored in this repository, by design.** GitHub rejects any single file over
100 MB and the PISA student file is 2.1 GB uncompressed. The repository holds code and the small
derived table; the raw inputs are downloadable from OECD (or the Drive mirror above). `data/` is
git-ignored.

Two of the seven published files are in scope:

| File | Unit of observation | Zipped | Unzipped |
|---|---|---|---|
| `CY09_MS_STU_PUF.sav` | one row per student | 947 MB | 2.1 GB |
| `CY09_MS_SCH_PUF.sav` | one row per school | 5.2 MB | 17.9 MB |

The remaining five (cognitive item responses, process logs, the Learning in the Digital World
assessment, and the timing/trend file) are out of scope — mostly because they are computer-
administration only, and Rwanda sat the assessment on paper.

## Reproducing

```bash
pip install pandas pyreadstat matplotlib
```

Place the two `.sav` files in `data/`, then run the extraction step (added shortly). It filters to
`CNT in ['MNG', 'RWA']`, keeps ~40 of ~1,750 columns, blanks PISA's coded non-responses, and
left-joins the school file onto the student file on `CNTSCHID` — producing one row per student,
saved as a small `.csv` that the analysis reads.

Three PISA rules the code respects: weight every estimate by `W_FSTUWT`; treat each subject's ten
plausible values (`PV1…PV10`) as ten draws rather than one score; and convert coded non-responses
(Valid Skip, Not Applicable, Invalid, No Response) to missing by matching each code's *label*, not
its numeric value.

## Notes

- Test mode differs between the two countries — Rwanda on paper, Mongolia on computer — so
  computer-only variables are structurally absent for Rwanda, and the mode difference is reported
  as a limitation rather than assumed away.
- GenAI was used as a working aid during this project and is cited in the submitted deliverables,
  per the course's Tier 4 policy.
