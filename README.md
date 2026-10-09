# PISA 2025: Mongolia vs. Rwanda

Final project for 90-819 Python Programming II at Carnegie Mellon University.

Brian Adjetey & Anar Amarjargal

## Research question

How does mathematics performance in PISA 2025 differ between Mongolia and Rwanda, and how is performance within each country associated with student socioeconomic status and school conditions? How do the two countries compare with OECD countries?

## Data

We use the PISA 2025 student and school public-use files from the OECD.

- `CY09_MS_STU_PUF.sav` - student file
- `CY09_MS_SCH_PUF.sav` - school file

The raw student file is too large for GitHub, so it is not stored in this repository. The notebook downloads both files directly from the shared Google Drive folder used for the project.

OECD source: https://www.oecd.org/en/data/datasets/pisa-2025-database.html

Shared files: https://drive.google.com/drive/folders/1Me0GPML6cYotrSabFRuJkklFSHpzSk8F?usp=drive_link

## Running the analysis

Open the notebook and run the cells from top to bottom. It downloads the two source files, cleans the variables used in the analysis, creates the comparison groups, calculates the weighted PISA results, and produces the tables and figures in the report.

The analysis uses student sampling weights and all 10 plausible values for the achievement estimates. The OECD group is used as a pooled comparison group rather than as an official OECD average.

## Repository files

- `Python_II_final_project_(Insight_report).ipynb` - full cleaning, analysis, and visualizations
- `results/` - summary tables from the analysis
- `requirements.txt` - Python packages used by the notebook
- `.gitignore` - keeps the large raw data files out of the repository
