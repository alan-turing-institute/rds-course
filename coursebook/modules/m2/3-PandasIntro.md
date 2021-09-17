---
jupytext:
  cell_metadata_filter: -all
  formats: md:myst
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.10.3
kernelspec:
  display_name: Python 3
  language: python
  name: python3
---

# Pandas intro

The Pandas library is a core part of the python data science ecosystem. It provides easy-to-use data structures and data analysis tools.

Pandas themselves have some great resources for getting started, including guides if you're coming from other software: https://pandas.pydata.org/pandas-docs/stable/getting_started/index.html#getting-started .

For now, we'll stick just to what we need for this course.

```python
import pandas as pd
```

Pandas has two main **labelled** data structures:
- Series

```{code-cell} ipython3
import pandas as pd
s = pd.Series([0.3, 4, 1, None, 9])
print(s)
```

- DataFrame

```{code-cell} ipython3
import numpy as np
import pandas as pd
df = pd.DataFrame(np.random.randn(10,2), index=np.arange(3, 13), columns=["random_A", "random_B"])
print(df)
```

Once we have data in these Pandas structures, we can perform some useful operations such as:
- `info()` - (`DataFrame` only) - prints a concice summary of a `DataFrame`
- `value_counts()` - returns a `Series` containing counts of unique values in the structure

+++

```{code-cell} ipython3
import numpy as np
import pandas as pd
s = pd.Series(np.random.randint(0,2,10))
print(s)
print() # blank line
print("value counts:")
print(s.value_counts())
```

We'll see more on how to use these structures, and other Pandas capabilities, later.
