# 2.9 Feature Engineering (TODO)



```python
import pandas as pd

df = pd.read_csv("data/ANSUR_II_FEMALE_Public.csv")
df.info()
df.head()
```

## Converting Units

```python
df["weightkg"].describe()
```

```python
df["stature"].describe()
```

## Creating New Features

```python
df["bmi"] = (df["weightkg"] / 10) / (df["stature"] / 1000)**2
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

```python

```
