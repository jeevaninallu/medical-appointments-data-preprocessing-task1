# medical-appointments-data-preprocessing-task1
Cleaned the “Medical Appointment No Shows” dataset using Python and Pandas. Tasks included handling invalid ages, converting dates, removing duplicates, standardizing column names, fixing data types, and transforming categorical fields.

## Dataset
I used the **Medical Appointment No Shows** dataset from Kaggle.

## Objective
Clean and prepare the raw dataset by handling invalid values, converting data types, standardizing formats, and removing duplicates to make it ready for analysis.

## Summary of steps performed:
1. Removed rows with negative Age values.
2. Converted the `Handicap` column values to binary (0 or 1).
3. Converted `ScheduledDay` and `AppointmentDay` to datetime format.
4. Converted `PatientId` from float to string for consistency.
5. Standardized all column names to lowercase and snake_case.
6. Converted `no_show` column values from "Yes"/"No" strings to binary (1 for no-show, 0 for show).
7. Removed rows where the appointment date is before the scheduled date.
8. Dropped duplicate records.
9. Dropped any rows with missing values.

## Files included
- `Task1.py` — Python script containing the cleaning steps.
- `KaggleV2-May-2016.csv` — Original dataset file.
- `cleaned_appointments.csv` — Cleaned dataset output.


