# 2.9 Feature Engineering (TODO)



```python
import pandas as pd

df = pd.read_csv("data/ANSUR_II_FEMALE_Public.csv")
df.info()
df.head()
```

## Converting Units

Despite the name, the `weightkg` column is in units of 100 grams, or tenths of a kilogram:

```python
df["weightkg"].describe()
```

And the `stature` (the person's height) column is in millimetres:

```python
df["stature"].describe()
```

For interpreting the data ourselves and presenting it to other it's helpful to have values on scales we're familiar with. It's quick to perform simple mathematical operations on columns with Pandas - let's convert the `weightkg` column to actually be in kilograms, and the `stature` column to be in metres:

```python
df["weightkg"] = df["weightkg"] / 10  # 100g -> kg
print("Median weight:", df["weightkg"].median(), "kg")

df["stature"] = df["stature"] / 1000  # mm -> metres
print("Median height:", df["stature"].median(), "m")
```

These look more familiar (at least if you're used to using the metric system!) We can also see that women in the army are lighter and taller on average compared to the general population ([73.1 kg median weight and 1.613 metres median height](https://www.cdc.gov/nchs/data/series/sr_03/sr03-046-508.pdf)), so we'd need to be careful not to generalise results from this data to the USA as a whole.


## Creating New Features



```python
df["bmi"] = df["weightkg"] / df["stature"]**2
df["bmi"].describe()
```

Link to higher order (polynomial) features


## Binning

- make things categorical
- when/why (including privacy/anonymisation)

```python

```

## Normalization

- when/why
- min-max, mean 0 std 1, ...

```python

```

## Transformation

- when/why
- types
- light touch only

```python

```

```python
df["bmi"].plot.hist(bins=20)
```

```python

df["Age"].plot.hist(bins=20)
```

```python
import numpy as np
import matplotlib.pyplot as plt

plt.hist(np.log(df["Age"]), bins=20)
```

```python
df.columns
```

## Feature Selection and Dimensionality Reduction

```python

```
