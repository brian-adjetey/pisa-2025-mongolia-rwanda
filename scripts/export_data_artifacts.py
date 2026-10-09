"""Export the raw analysis extracts and cleaned analysis files required for submission.

This script mirrors the variable selection, grouping, renaming, and missing-code
cleaning already used in the final notebook. It does not calculate or modify any
reported results.

Usage:
    python scripts/export_data_artifacts.py --download

Or, if the two PISA .sav files are already present:
    python scripts/export_data_artifacts.py \
        --student CY09_MS_STU_PUF.sav \
        --school CY09_MS_SCH_PUF.sav
"""

from pathlib import Path
import argparse

import gdown
import numpy as np
import pandas as pd


STUDENT_DRIVE_ID = "163VOjSHyLiuVDj4pZRX9g5sSeMBn3FXO"
SCHOOL_DRIVE_ID = "1VZyjoUiPhUBnxFBOJPqmRBDjAmGg0smZ"

STUDENT_COLUMNS = [
    "CNT", "OECD", "CNTSCHID", "CNTSTUID",
    "ESCS", "MALE", "REPEAT", "W_FSTUWT",
    *[f"PV{i}MATH" for i in range(1, 11)],
    *[f"PV{i}READ" for i in range(1, 11)],
    *[f"PV{i}SCIE" for i in range(1, 11)],
]

SCHOOL_COLUMNS = [
    "CNT", "OECD", "CNTSCHID", "SC001Q01TA", "EDUSHORT", "STAFFSHORT"
]


def add_analysis_group(data):
    """Create the same analysis-group variable used in the final notebook."""
    return data.assign(
        analysis_group=np.select(
            [
                data["country"] == "MNG",
                data["country"] == "RWA",
                data["is_oecd"] == 1,
            ],
            ["Mongolia", "Rwanda", "OECD"],
            default="Other",
        )
    )


def target_raw_rows(data):
    """Keep exactly the Mongolia, Rwanda, and OECD records used in the analysis."""
    return data[
        (data["CNT"] == "MNG")
        | (data["CNT"] == "RWA")
        | (data["OECD"] == 1)
    ].copy()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--student", default="CY09_MS_STU_PUF.sav")
    parser.add_argument("--school", default="CY09_MS_SCH_PUF.sav")
    parser.add_argument("--output-dir", default="data")
    parser.add_argument(
        "--download",
        action="store_true",
        help="Download the two source files from the project Google Drive if absent.",
    )
    args = parser.parse_args()

    student_path = Path(args.student)
    school_path = Path(args.school)
    output_dir = Path(args.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    if args.download:
        if not student_path.exists():
            gdown.download(id=STUDENT_DRIVE_ID, output=str(student_path))
        if not school_path.exists():
            gdown.download(id=SCHOOL_DRIVE_ID, output=str(school_path))

    if not student_path.exists() or not school_path.exists():
        raise FileNotFoundError(
            "PISA source files were not found. Supply --student/--school paths "
            "or run with --download."
        )

    # Read the same source variables selected in the final notebook.
    student_raw = pd.read_spss(
        student_path,
        usecols=STUDENT_COLUMNS,
        convert_categoricals=False,
    )
    school_raw = pd.read_spss(
        school_path,
        convert_categoricals=False,
    )[SCHOOL_COLUMNS]

    # Save uncleaned analysis extracts with original PISA names and values.
    raw_student_extract = target_raw_rows(student_raw)
    raw_school_extract = target_raw_rows(school_raw)

    raw_student_extract.to_csv(
        output_dir / "raw_student_analysis_extract.csv.gz",
        index=False,
        compression="gzip",
    )
    raw_school_extract.to_csv(
        output_dir / "raw_school_analysis_extract.csv.gz",
        index=False,
        compression="gzip",
    )

    # Rename exactly as in the final notebook.
    school_clean = school_raw.rename(
        columns={
            "CNT": "country",
            "OECD": "is_oecd",
            "CNTSCHID": "school_id",
            "SC001Q01TA": "school_location",
            "EDUSHORT": "edu_material_shortage",
            "STAFFSHORT": "staff_shortage",
        }
    )

    student_rename = {
        "CNT": "country",
        "OECD": "is_oecd",
        "CNTSCHID": "school_id",
        "CNTSTUID": "student_id",
        "MALE": "is_male",
        "ESCS": "socioeconomic_index",
        "REPEAT": "grade_repetition",
        "W_FSTUWT": "student_weight",
    }
    for i in range(1, 11):
        student_rename[f"PV{i}MATH"] = f"math{i}"
        student_rename[f"PV{i}READ"] = f"read{i}"
        student_rename[f"PV{i}SCIE"] = f"science{i}"

    student_clean = student_raw.rename(columns=student_rename)

    school_clean = add_analysis_group(school_clean)
    student_clean = add_analysis_group(student_clean)

    # Apply the same project missing-code rules as the final notebook.
    missing_95_99 = [95, 96, 97, 98, 99]
    missing_repeat = [5, 6, 7, 8, 9]
    missing_plausible_value = [9997]
    missing_school_id = ["9999997"]

    school_missing_values = {
        "school_id": missing_school_id,
        "school_location": missing_95_99,
        "edu_material_shortage": missing_95_99,
        "staff_shortage": missing_95_99,
    }
    for column, missing_codes in school_missing_values.items():
        school_clean[column] = school_clean[column].replace(missing_codes, np.nan)

    student_missing_values = {
        "school_id": missing_school_id,
        "socioeconomic_index": missing_95_99,
        "is_male": missing_95_99,
        "grade_repetition": missing_repeat,
    }
    for i in range(1, 11):
        student_missing_values[f"math{i}"] = missing_plausible_value
        student_missing_values[f"read{i}"] = missing_plausible_value
        student_missing_values[f"science{i}"] = missing_plausible_value

    for column, missing_codes in student_missing_values.items():
        student_clean[column] = student_clean[column].replace(missing_codes, np.nan)

    target_groups = ["Mongolia", "Rwanda", "OECD"]
    student_clean = student_clean[
        student_clean["analysis_group"].isin(target_groups)
    ].copy()
    school_clean = school_clean[
        school_clean["analysis_group"].isin(target_groups)
    ].copy()

    # Integrity: cleaning and renaming must not change the analysis-sample row counts.
    assert len(student_clean) == len(raw_student_extract)
    assert len(school_clean) == len(raw_school_extract)
    assert school_clean["school_id"].dropna().is_unique

    student_clean.to_csv(
        output_dir / "cleaned_student_analysis.csv.gz",
        index=False,
        compression="gzip",
    )
    school_clean.to_csv(
        output_dir / "cleaned_school_analysis.csv.gz",
        index=False,
        compression="gzip",
    )

    print("Exported data artifacts:")
    for path in sorted(output_dir.glob("*.csv.gz")):
        print(f"- {path} ({path.stat().st_size / 1_000_000:.1f} MB)")


if __name__ == "__main__":
    main()
