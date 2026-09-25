# PISA 2025: Mongolia vs. Rwanda

What factors may explain differences in PISA performance between **Mongolia** and **Rwanda**?

Final project for 90-819 Python Programming II, Carnegie Mellon University.
Brian Adjetey & Anar Amarjargal.

## Data

All data comes from the **OECD Programme for International Student Assessment (PISA), 2025 cycle**.
Both countries participated: Rwanda for the first time, Mongolia as a partner country.

| What | Where |
|---|---|
| Original source | [OECD PISA 2025 Database](https://www.oecd.org/en/data/datasets/pisa-2025-database.html) |
| The two raw files we use, zipped | [Google Drive folder](https://drive.google.com/drive/folders/1Me0GPML6cYotrSabFRuJkklFSHpzSk8F?usp=drive_link) |

Two of the seven published files are in scope:

| File | Unit of observation | Zipped | Unzipped |
|---|---|---|---|
| `CY09_MS_STU_PUF.sav` | one row per student | 947 MB | 2.1 GB |
| `CY09_MS_SCH_PUF.sav` | one row per school | 5.2 MB | 17.9 MB |

The raw files are not stored in this repository: GitHub caps single files at 100 MB and the student
file is 2.1 GB uncompressed. Download them from OECD or the Drive folder above and place them in
`data/`, which is git-ignored.

## Setup

```bash
pip install pandas pyreadstat matplotlib
```

The `.sav` files are SPSS format and load directly into pandas via `pyreadstat` — no SPSS licence or
conversion step needed. The analysis filters to `CNT in ['MNG', 'RWA']`, keeps about 40 of roughly
1,750 columns, and left-joins the school file onto the student file on `CNTSCHID`.
