"""
Loads the Iris data and adds some rows to represent issues that can
arise with data consistency.
"""
import pandas as pd
import numpy as np

df = pd.read_csv("penguins_original.csv")
print("\nOriginal data frame info:\n")
df.info()

new = df.copy()

# create a dummy ID column of format P-000
new["Id"] = "P-" + new.index.astype(str).str.zfill(3)

# make ID the first column
new = new[
    [
        "Id",
        "species",
        "island",
        "bill_length_mm",
        "bill_depth_mm",
        "flipper_length_mm",
        "body_mass_g",
        "sex",
        "year",
    ]
]

# Correctly treated missing values (NaN bill_length_mm)
new = new.append(
    {
        "Id": "P-344",
        "species": "Chinstrap",
        "island": "Dream",
        "bill_length_mm": np.nan,
        "bill_depth_mm": 19.2,
        "flipper_length_mm": 197,
        "body_mass_g": 4000,
        "sex": "male",
        "year": 2008,
    },
    ignore_index=True,
)

new = new.append(
    {
        "Id": "P-345",
        "species": "Adelie",
        "island": "Torgersen",
        "bill_length_mm": np.nan,
        "bill_depth_mm": 18.0,
        "flipper_length_mm": 193,
        "body_mass_g": 43400,
        "sex": "female",
        "year": 2009,
    },
    ignore_index=True,
)

# comma instead of decimal point (bill_depth_mm 14,2 instead of 14.2)
new = new.append(
    {
        "Id": "P-346",
        "species": "Gentoo",
        "island": "Biscoe",
        "bill_length_mm": 45.2,
        "bill_depth_mm": "14,2",
        "flipper_length_mm": 224,
        "body_mass_g": 5600,
        "sex": "male",
        "year": 2007,
    },
    ignore_index=True,
)

# missing value encoded as negative number (-99 for flipper_length_mm)
new = new.append(
    {
        "Id": "P-347",
        "species": "Adelie",
        "island": "Dream",
        "bill_length_mm": 36.0,
        "bill_depth_mm": 17.3,
        "flipper_length_mm": -99,
        "body_mass_g": 3475,
        "sex": "female",
        "year": 2007,
    },
    ignore_index=True,
)

# suspiciously low value, perhaps a typo (body_mass_g = 285 instead of 2850)
new = new.append(
    {
        "Id": "P-348",
        "species": "Adelie",
        "island": "Biscoe",
        "bill_length_mm": 36.4,
        "bill_depth_mm": 18.1,
        "flipper_length_mm": 193,
        "body_mass_g": 285,
        "sex": "female",
        "year": 2007,
    },
    ignore_index=True,
)

# UNKNOWN Speciees
new = new.append(
    {
        "Id": "P-349",
        "species": "UNKNOWN",
        "island": "Biscoe",
        "bill_length_mm": 55.9,
        "bill_depth_mm": 15.9,
        "flipper_length_mm": 218,
        "body_mass_g": 5300,
        "sex": "male",
        "year": 2009,
    },
    ignore_index=True,
)

# duplicate row
new = new.append(
    {
        "Id": "P-276",
        "species": "Chinstrap",
        "island": "Dream",
        "bill_length_mm": 46.5,
        "bill_depth_mm": 17.9,
        "flipper_length_mm": 192,
        "body_mass_g": 3500,
        "sex": "female",
        "year": 2007,
    },
    ignore_index=True,
)

# shuffle data frame order so added strange values not so obvious
new = new.sample(frac=1, random_state=123)

print("\nUpdated data frame info:\n")
new.info()

new.to_csv("penguins.csv", index=False)
