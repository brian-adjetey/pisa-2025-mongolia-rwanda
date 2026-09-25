# PISA 2025: Mongolia vs. Rwanda

Students in Mongolia and Rwanda sat the same international school test in 2025 and scored
differently. This project looks at what might explain that gap — things about the students
themselves, and things about the schools they attend.

Final project for 90-819 Python Programming II, Carnegie Mellon University.
Brian Adjetey & Anar Amarjargal.

## The data

The test is PISA, run every three years by the OECD. It is given to 15-year-olds and covers
reading, maths, and science. Around 80 countries took part in the 2025 round, including both of
ours — Rwanda for the first time, Mongolia as a partner country. Anyone can download the results
for free.

| What | Where |
|---|---|
| The official download page | [OECD PISA 2025 Database](https://www.oecd.org/en/data/datasets/pisa-2025-database.html) |
| A copy of the two files we use | [Google Drive folder](https://drive.google.com/drive/folders/1Me0GPML6cYotrSabFRuJkklFSHpzSk8F?usp=drive_link) |

The OECD splits the results into seven files. We only need two of them:

| File | What one row is | Download size | Size once unzipped |
|---|---|---|---|
| `CY09_MS_STU_PUF.sav` | one student | 947 MB | 2.1 GB |
| `CY09_MS_SCH_PUF.sav` | one school | 5.2 MB | 17.9 MB |

The other five are much bigger and are not useful to us. Most of them were only collected from
students who took the test on a computer, and Rwandan students took it on paper.

**The data files themselves are not in this repository.** GitHub refuses any file bigger than
100 MB, and the student file is 2.1 GB. Download the two files from either link above and put them
in a folder called `data` — this project is set up to leave that folder alone, so the big files
never get uploaded here by accident.

## Getting set up

```bash
pip install pandas pyreadstat matplotlib
```

The files end in `.sav`, which is the format used by a statistics program called SPSS. You do not
need that program: the `pyreadstat` package opens these files in Python as an ordinary table, the
same kind of table pandas uses everywhere else.

From there the work is mostly narrowing things down. The files hold every country, so we keep only
the Mongolian and Rwandan rows. They hold about 1,750 columns between them, so we keep the 40 or so
we actually need. And each student's school is listed separately, so we copy each school's details
onto the rows of the students who attend it. What comes out is one small table with one row per
student, which is what the rest of the analysis reads.
