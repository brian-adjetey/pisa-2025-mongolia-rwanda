# PISA 2025: Mongolia vs. Rwanda

Final project for **90-819 Python Programming II** at Carnegie Mellon University.

**Authors:** Brian Adjetey and Anar Amarjargal

## Research question

How does mathematics performance in PISA 2025 differ between Mongolia and Rwanda, and how is performance within each country associated with student socioeconomic status and school conditions? How do the two countries compare with a pooled OECD comparison group?

The analysis is descriptive rather than causal. It uses PISA student sampling weights and all 10 plausible values for mathematics, reading, and science.

## Data

The project uses the OECD PISA 2025 public-use student and school files.

| File | Unit of observation | Approx. uncompressed size |
|---|---|---:|
| `CY09_MS_STU_PUF.sav` | Student | 2.1 GB |
| `CY09_MS_SCH_PUF.sav` | School | 17.9 MB |

- [OECD PISA 2025 database](https://www.oecd.org/en/data/datasets/pisa-2025-database.html)
- [Google Drive copy used by the notebook](https://drive.google.com/drive/folders/1Me0GPML6cYotrSabFRuJkklFSHpzSk8F?usp=drive_link)

The raw `.sav` files are not committed to GitHub because the student file exceeds GitHub's file-size limit. The notebook downloads both files automatically with `gdown`, so the analysis can still be reproduced from the repository.

## Repository structure

```text
.
├── PISA_2025_Mongolia_Rwanda_Insight_Report.ipynb
├── cleaned_data/
│   ├── student_analysis_clean.parquet
│   └── school_analysis_clean.parquet
├── results/
│   └── *.csv
├── requirements.txt
├── README.md
└── .gitignore
```

`cleaned_data/` contains the analysis-ready datasets exported by the notebook. `results/` contains the main summary tables used in the report.

## Reproduce the analysis

1. Clone or download this repository.
2. Install the dependencies:

```bash
pip install -r requirements.txt
```

3. Open `PISA_2025_Mongolia_Rwanda_Insight_Report.ipynb` in Google Colab or Jupyter.
4. Run the notebook from top to bottom.

The notebook will:
- download the two PISA public-use files;
- select the required student and school variables;
- recode missing values and define Mongolia, Rwanda, and OECD comparison groups;
- calculate weighted achievement estimates across all 10 plausible values;
- compare student and school characteristics;
- examine mathematics performance by gender, grade repetition, ESCS, school location, and educational material shortages;
- calculate weighted correlations with ESCS, material shortages, and staff shortages;
- generate the report visualizations;
- export cleaned analysis datasets and result tables.

## Methodological note

The OECD comparison is a pooled comparison group based on the student sampling weights in the selected OECD observations; it should not be interpreted as the official equal-country OECD average. The project reports descriptive associations and does not make causal claims. Formal PISA replicate-weight standard errors and hypothesis tests are outside the scope of this course project.
