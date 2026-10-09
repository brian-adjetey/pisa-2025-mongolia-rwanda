# PISA 2025: Mongolia vs. Rwanda

Final project for 90-819 Python Programming II at Carnegie Mellon University.

Brian Adjetey & Anar Amarjargal

## Research question

How does mathematics performance in PISA 2025 differ between Mongolia and Rwanda, and how is performance within each country associated with student socioeconomic status and school conditions? How do the two countries compare with OECD countries?

## Data

We use the PISA 2025 student and school public-use files from the OECD.

- `CY09_MS_STU_PUF.sav` - student file
- `CY09_MS_SCH_PUF.sav` - school file

The complete student public-use file is approximately 2.17 GB and exceeds GitHub's normal file-size limit. The notebook downloads the original source files directly. The `data/` directory documents the source files and the analysis extracts/cleaned files used for reproducibility.

OECD source: https://www.oecd.org/en/data/datasets/pisa-2025-database.html

Shared project files: https://drive.google.com/drive/folders/1Me0GPML6cYotrSabFRuJkklFSHpzSk8F?usp=drive_link

## Running the analysis

1. Install the packages in `requirements.txt`.
2. Open `Python_II_final_project_(Insight_report).ipynb`.
3. Run the notebook from top to bottom.

The notebook downloads the source files, selects and cleans the variables used in the analysis, creates the comparison groups, calculates the weighted PISA results, and produces the tables and figures in the report.

To regenerate the compressed raw-analysis extracts and cleaned-data files required for submission, run:

```bash
python scripts/export_data_artifacts.py --download
```

Achievement estimates use the final student sampling weight (`W_FSTUWT`). Statistics are calculated separately for each of the 10 plausible values and then averaged. The OECD group is a pooled weighted comparison group rather than the official equal-country OECD average. The analysis is descriptive and associational; formal PISA standard errors and hypothesis tests are not reported because full inference requires replicate-weight procedures beyond the scope of this project.

## Repository files

- `Python_II_final_project_(Insight_report).ipynb` - full data cleaning, analysis, and visualizations
- `python ii final proj report.pdf` - final reader-facing insight report
- `data/README.md` - source-data and reproducibility notes
- `data/DATA_DICTIONARY.md` - variables and transformations used in the analysis
- `data/raw_*_analysis_extract.csv.gz` - uncleaned analysis extracts retaining original PISA variable names and values
- `data/cleaned_*_analysis.csv.gz` - cleaned analysis files used by the notebook
- `scripts/export_data_artifacts.py` - reproducibly generates the compressed raw and cleaned analysis files
- `results/` - summary tables generated from the analysis
- `requirements.txt` - Python packages used by the notebook
- `.gitignore` - excludes full raw `.sav` files and temporary files

## Sources

- OECD. *PISA 2025 Database.* https://www.oecd.org/en/data/datasets/pisa-2025-database.html
- OECD. *PISA Research Documentation: How to Prepare and Analyse the PISA Database.* https://www.oecd.org/en/about/programmes/pisa/how-to-prepare-and-analyse-the-pisa-database.html
- National Institute of Statistics of Rwanda. *Fifth Rwanda Population and Housing Census 2022: Main Indicators Report.* https://alpha.statistics.gov.rw/sites/default/files/documents/2025-02/RPHC5_MainIndicatorsReport_Final.pdf

## Generative AI acknowledgment

ChatGPT and OpenAI Codex were used for Python debugging, code review, data-quality auditing, reproducibility checks, and editorial feedback. The authors reviewed the code, verified the calculations against the underlying PISA data, and are responsible for the final analysis and interpretation.
