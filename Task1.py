# I used the "Medical Appointment No Shows" dataset from Kaggle.

import pandas as pd
df = pd.read_csv(r"C:\Users\nallu\OneDrive\Documents\SEMESTERS\Tasks\KaggleV2-May-2016.csv")  # Load the dataset

print(df.head())           # Display first few rows
print(df.info())           # Show data types and non-null counts
print(df.describe())       # Summary statistics of numeric columns

# Step 1:
# Based on the dataset info, I observed that the 'Age' column has an integer type.
df = df[df['Age'] >= 0]  # Removed rows with negative age values

# Step 2:
# 'Handcap' column has values greater than 1, which is unusual for binary data.
df['Handcap'] = df['Handcap'].apply(lambda x: 1 if x > 0 else 0)  # Convert to binary (0 or 1)

# Step 3:
# Convert 'ScheduledDay' and 'AppointmentDay' from strings to datetime
df['ScheduledDay'] = pd.to_datetime(df['ScheduledDay'], errors='coerce')
df['AppointmentDay'] = pd.to_datetime(df['AppointmentDay'], errors='coerce')

# Step 4:
# 'PatientId' should not be a float; converting to string for consistency
df['PatientId'] = df['PatientId'].astype(str)

# Step 5:
# Standardize column names to lowercase and snake_case
df.columns = [col.strip().lower().replace('-', '_').replace(' ', '_') for col in df.columns]

# Step 6:
# Convert 'no_show' column from 'Yes/No' to binary format (1 for No-show, 0 for Show)
df['no_show'] = df['no_show'].map({'No': 0, 'Yes': 1})

# Step 7:
# Remove rows where appointment is scheduled after the appointment date
df = df[df['appointmentday'] >= df['scheduledday']]

# Step 8:
# Remove duplicate rows
df = df.drop_duplicates()

# Step 9:
# Drop any missing values if present 
df = df.dropna()

# cleaned dataset
df.to_csv("cleaned_appointments.csv", index=False)
