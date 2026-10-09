# Data files

This project uses the OECD PISA 2025 public-use student and school files.

## Original source files

- `CY09_MS_STU_PUF.sav` - PISA 2025 student questionnaire/public-use file
- `CY09_MS_SCH_PUF.sav` - PISA 2025 school questionnaire/public-use file

Official source: https://www.oecd.org/en/data/datasets/pisa-2025-database.html

The complete student file is approximately 2.17 GB, which exceeds GitHub's normal per-file size limit. The full `.sav` files are therefore not committed to this repository. The analysis notebook downloads the original files directly before processing them.

To make the exact analysis sample auditable without committing the multi-gigabyte source file, the repository uses compressed analysis extracts:

- `raw_student_analysis_extract.csv.gz` - original PISA names/values for the student variables and analysis groups used in this project, before project missing-code recoding
- `raw_school_analysis_extract.csv.gz` - original PISA names/values for the school variables and analysis groups used in this project, before project missing-code recoding
- `cleaned_student_analysis.csv.gz` - renamed student variables after the project's missing-code cleaning and analysis-group construction
- `cleaned_school_analysis.csv.gz` - renamed school variables after the project's missing-code cleaning and analysis-group construction

Only Mongolia, Rwanda, and the pooled OECD comparison sample are retained in these extracts because those are the observations used in the reported analysis. The full public-use files remain available from OECD.

## Cleaning rules

The notebook is the authoritative cleaning code. In summary:

- PISA special missing codes 95-99 are mapped to missing where applicable.
- `REPEAT` special codes 5-9 are mapped to missing.
- plausible-value code `9997` is mapped to missing.
- school ID `9999997` is mapped to missing.
- `analysis_group` is derived as Mongolia (`CNT == "MNG"`), Rwanda (`CNT == "RWA"`), or OECD (`OECD == 1`).
- The OECD benchmark is pooled with student sampling weights; it is not the official equal-country OECD average.

See `DATA_DICTIONARY.md` for variable definitions and the notebook for the complete executable workflow.
