"""
Loads the Iris data and adds some rows to represent issues that can
arise with data consistency.
"""
import pandas as pd
import numpy as np

df = pd.read_csv("Iris_original.csv")
print("\nOriginal data frame info:\n")
df.info()

new = df.copy()

# missing value encoded as negative number (-99 for SepalLengthCm)
new = new.append(
    {
        "Id": 151,
        "SepalLengthCm": -99,
        "SepalWidthCm": 3.4,
        "PetalLengthCm": 5.0,
        "PetalWidthCm": 5.0,
        "Species": "Iris-virginica",
    },
    ignore_index=True,
)

# UNKNOWN Speciees
new = new.append(
    {
        "Id": 152,
        "SepalLengthCm": 6.3,
        "SepalWidthCm": 3.0,
        "PetalLengthCm": 4.9,
        "PetalWidthCm": 2.3,
        "Species": "UNKNOWN",
    },
    ignore_index=True,
)

# duplicate row
new = new.append(
    {
        "Id": 53,
        "SepalLengthCm": 6.9,
        "SepalWidthCm": 3.1,
        "PetalLengthCm": 4.9,
        "PetalWidthCm": 1.5,
        "Species": "Iris-versicolor",
    },
    ignore_index=True,
)

# comma instead of decimal point (SepalWidthCm 3,1 instead of 3.1)
new = new.append(
    {
        "Id": 153,
        "SepalLengthCm": 5.0,
        "SepalWidthCm": "3,1",
        "PetalLengthCm": 1.3,
        "PetalWidthCm": 0.2,
        "Species": "Iris-setosa",
    },
    ignore_index=True,
)

# missing decimal point (PetalLengthCm = 40 instead of 4.0)
new = new.append(
    {
        "Id": 154,
        "SepalLengthCm": 6.0,
        "SepalWidthCm": 2.9,
        "PetalLengthCm": 40,
        "PetalWidthCm": 1.7,
        "Species": "Iris-versicolor",
    },
    ignore_index=True,
)

# Correctly treated missing values (NaN PetalWidthCm)
new = new.append(
    {
        "Id": 155,
        "SepalLengthCm": 5.0,
        "SepalWidthCm": 3.9,
        "PetalLengthCm": 1.5,
        "PetalWidthCm": np.nan,
        "Species": "Iris-setosa",
    },
    ignore_index=True,
)

new = new.append(
    {
        "Id": 156,
        "SepalLengthCm": 6.6,
        "SepalWidthCm": 3.0,
        "PetalLengthCm": 4.8,
        "PetalWidthCm": np.nan,
        "Species": "Iris-versicolor",
    },
    ignore_index=True,
)

# shuffle order so added strange values not so obvious
new = new.sample(frac=1, random_state=123)

print("\nUpdated data frame info:\n")
new.info()

new.to_csv("Iris.csv", index=False)
