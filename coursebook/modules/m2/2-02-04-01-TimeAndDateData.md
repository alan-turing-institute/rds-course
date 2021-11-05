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
  display_name: Python 3 (ipykernel)
  language: python
  name: python3
---

# 2.2.4.1 Time and Date Data

Dealing with time and date data can be tricky. String-formatted data is hard to compare and represent for modelling.

```{code-cell} ipython3
print("02/03/1900" > "01/01/2020")
```

We use the `datetime.datetime` object in examples below. However, you can also use `datetime.date` and `datetime.time` as appropriate.

## datetime

We need to represent this data in a format that will allow us to compare items and perform operations such as addition and subtraction.

Python's standard library includes the [`datetime`](https://docs.python.org/3/library/datetime.html) module.
This allows us to represent dates and times as structured objects.

```{code-cell} ipython3
import datetime
# create a datetime object with value set to now
now = datetime.datetime.now()
print(now)
```

This object has structure. We can, for example, extract the year property from this object.

```{code-cell} ipython3
print(now.year)
```

We can also compare this datetime to others, as well as performing date arithmetic.

```{code-cell} ipython3
past = datetime.datetime.fromisoformat("2020-12-22")
is_gt_now = past > now
print(f"d gt now: {is_gt_now}")

# subtract past from now
difference = now - past
print(f"now - d: {difference}. Type: {type(difference)}")
```

We can get a numeric, [POSIX timestamp](https://en.wikipedia.org/wiki/Unix_time), representation of these dates with `datetime.datetime.timestamp()`.

```{code-cell} ipython3
print(f"now timestamp: {now.timestamp()}")
print(f"past timestamp: {past.timestamp()}")
```

Note some UTC vs local time complications detailed [here](https://docs.python.org/3/library/datetime.html#datetime.datetime.timestamp).

## Converting From/To String

For converting *from* a string, we can use the `datetime.datetime.strptime(date_string, format)` function. Format codes are detailed [here](https://docs.python.org/3/library/datetime.html#strftime-and-strptime-format-codes).

```{code-cell} ipython3
dt = datetime.datetime.strptime("30/03/99 16:30", "%d/%m/%y %H:%M")
print(f"{dt}. Type: {type(dt)}")
```

And to convert a date *to* string we can use `datetime.datetime.strftime(format)`.

```{code-cell} ipython3
s = now.strftime("%d/%m/%y %H:%M")
print(f"{s}. Type: {type(s)}")
```
