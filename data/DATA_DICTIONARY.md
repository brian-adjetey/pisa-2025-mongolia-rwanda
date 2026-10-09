# Data dictionary

This dictionary covers the variables used in the final PISA 2025 Mongolia-Rwanda analysis. Source names refer to the OECD public-use files; cleaned names are the names used in the notebook.

## Student variables

| Source variable | Cleaned variable | Meaning / use |
|---|---|---|
| `CNT` | `country` | PISA country/economy code. `MNG` = Mongolia; `RWA` = Rwanda. |
| `OECD` | `is_oecd` | OECD membership indicator supplied in the PISA file. Used to construct the pooled OECD comparison group. |
| `CNTSCHID` | `school_id` | PISA school identifier used to link students to school characteristics. Special code `9999997` is treated as missing. |
| `CNTSTUID` | `student_id` | PISA student identifier. |
| `MALE` | `is_male` | Gender indicator used in the public-use file. `1` = male; `0` is labeled `Female/Other` in this project. Special missing codes are set to missing. |
| `ESCS` | `socioeconomic_index` | PISA index of economic, social and cultural status (ESCS). Higher values indicate higher socioeconomic status. Special codes 95-99 are treated as missing. |
| `REPEAT` | `grade_repetition` | Grade-repetition indicator. `1` = reports having repeated a grade; `0` = no reported repetition. Special codes 5-9 are treated as missing. |
| `W_FSTUWT` | `student_weight` | Final student sampling weight used for weighted student-level estimates. |
| `PV1MATH`-`PV10MATH` | `math1`-`math10` | Ten mathematics plausible values. `9997` is treated as missing. |
| `PV1READ`-`PV10READ` | `read1`-`read10` | Ten reading plausible values. `9997` is treated as missing. |
| `PV1SCIE`-`PV10SCIE` | `science1`-`science10` | Ten science plausible values. `9997` is treated as missing. |

## School variables

| Source variable | Cleaned variable | Meaning / use |
|---|---|---|
| `CNT` | `country` | PISA country/economy code. |
| `OECD` | `is_oecd` | OECD membership indicator supplied in the PISA school file. |
| `CNTSCHID` | `school_id` | PISA school identifier. The school file is checked for uniqueness before the student-school merge. |
| `SC001Q01TA` | `school_location` | Reported population-size category of the community in which the school is located. Original categories are retained for audit; broad groups are derived for the final analysis. |
| `EDUSHORT` | `edu_material_shortage` | PISA educational-material-shortage index. Higher values indicate greater reported shortage. |
| `STAFFSHORT` | `staff_shortage` | PISA staff-shortage index. Higher values indicate greater reported shortage. |

## Derived variables

| Variable | Construction | Meaning / use |
|---|---|---|
| `analysis_group` | Mongolia when `country == "MNG"`; Rwanda when `country == "RWA"`; OECD when `is_oecd == 1`; otherwise `Other` | Defines the three reported comparison groups. The OECD group is pooled and student-weighted rather than an official equal-country OECD average. |
| `escs_range` | ESCS bins: below -2; -2 to -1; -1 to 0; 0 to 1; above 1 | Used for descriptive mathematics comparisons across common socioeconomic ranges. |
| `material_shortage_category` | `EDUSHORT`/cleaned index binned as Low (< -0.5), Moderate (-0.5 to 0.5), High (> 0.5) | Used for descriptive mathematics comparisons by material-shortage level. |
| `school_location_group` | Raw location 1 = Rural (<3,000); 2-3 = Town (3,000-100,000); 4-6 = Urban (>100,000) | Broad grouping used because Rwanda contains anomalous raw category-6 responses. |
| `urban_status` | Location 4-6 = Urban (>100,000); 1-3 = Rural/Town (<100,000) | Used only for the Rwanda location sensitivity check. |

## Raw school-location codes

| Code | International label used in the PISA file |
|---:|---|
| 1 | Village/Rural (<3,000) |
| 2 | Small Town (3,000-15,000) |
| 3 | Town (15,000-100,000) |
| 4 | City (100,000-1M) |
| 5 | Large City (1M-10M) |
| 6 | Megacity (>10M) |

Eleven Rwandan schools (346 linked students) have raw code 6. The final report retains the original values for audit, groups them only at the broad urban level, and reports a sensitivity check excluding those observations from the location comparison.

## Achievement estimation

For achievement means, subgroup means, and correlations, the statistic is calculated separately for each of the 10 relevant plausible values using `student_weight`, and the 10 resulting estimates are then averaged. Formal standard errors and hypothesis tests are not reported because full PISA inference requires replicate-weight procedures beyond the scope of this descriptive project.
