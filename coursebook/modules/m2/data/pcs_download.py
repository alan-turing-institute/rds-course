"""
Download New York State 2017 Patient Characteristics Survey (PCS) and save a subset of
it.
"""
import pandas as pd

df = pd.read_csv(
    "https://data.ny.gov/api/views/8itk-gcdy/rows.csv?accessType=DOWNLOAD&sorting=true"
)

# only include these columns
select_columns = [
    "Program Category",
    "Region Served",
    "Age Group",
    "Sex",
    "Living Situation",
    "Household Composition",
    "Preferred Language",
    "Veteran Status",
    "Employment Status",
    "Number Of Hours Worked Each Week",
    "Education Status",
    "Special Education Services",
    "Mental Illness",
    "Intellectual Disability",
    "Autism Spectrum",
    "Alcohol Related Disorder",
    "Drug Substance Disorder",
    "Mobility Impairment Disorder",
    "Alzheimer or Dementia",
    "Neurological Condition",
    "Traumatic Brain Injury",
    "Cancer",
    "Smokes",
    "Received Smoking Medication",
    "Received Smoking Counseling",
    "Serious Mental Illness",
    "Principal Diagnosis Class",
    "SSI Cash Assistance",
    "SSDI Cash Assistance",
    "Public Assistance Cash Program",
    "Other Cash Benefits",
    "Three Digit Residence Zip Code",
]
df = df[select_columns]

# save a subset of 5000 patients only (full dataset is >80 MB)
df = df.sample(n=5000, random_state=123)
df.to_csv("pcs_2017.csv", index=False)
