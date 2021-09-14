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

# Wrangling text data

TODO preamble

## Inconsistencies

Text data (strings) have their own particular array of consistency issues, such as inconsistent capitalisation and extraneous whitespace. 

Fortunately, python gives us some handy [built-in functionality](https://docs.python.org/3/library/stdtypes.html#string-methods) for dealing with some of these issues.

We'll make note of a few of these methods, below.

### `str.upper()` and `str.lower()`

The `str.upper()` and `str.lower()` methods will take a given string and return a copy as a solely uppercase or lowercase string. E.g.

```{code-cell} ipython3
print(f"upper: {'Foo'.upper()}")
print(f"lower: {'Foo'.lower()}")
```

These methods can be useful for ensuring consistency when casing is not important in your data.

### `str.strip()`

The `str.strip()` method (and it's companions, `str.lstrip` and `str.rstrip()`) return a copy, stripping leading and trailing characters (default to whitespace) from a string. E.g.

```{code-cell} ipython3
stripped = " foo bar ".strip()

print(f"stripped: '{stripped}'")
lstripped = " foo bar ".lstrip() # strip left
print(f"left stripped: '{lstripped}'")

rstripped = " foo bar ".rstrip() # strip right
print(f"right stripped: '{rstripped}'")
```

### Spelling is tricky

The methods we've talked about so far don't address things like misspelling/typos (a common data input concern). 

In a relatively simple scenario, with categorical data encoded as strings, you might be able to spot these by checking for all unique values in your data. E.g.

```{code-cell} ipython3
my_favourite_fruit_data = ["apple", "apple", "pear", "orange", "aple", "orange", "grapefruit"]
print(set(my_favourite_fruit_data))
```

## Regular expressions

[Regular expressions (regexps, regex)](https://en.wikipedia.org/wiki/Regular_expression) are character sequences that specify a search pattern, usually for a find and/or replace task on text data.

Python's [regular expression](https://docs.python.org/3/library/re.html) module provides functionality similar to that offered in Perl.

Regex can give us powerful string matching, beyond that of a simple exact string match. E.g.

```{code-cell} ipython3
import re
txt = "The rain in Spain falls mainly on the plains. So they say, anyway."
# find all words starting with upper case S or lower case t
print(re.findall(r"\b[St]\w+", txt))
```


## NLP preprocessing

In Natural Language Processing (NLP) tasks we often see some slightly more complicated preprocessing such as:

- [Stemming and Lemmatisation](https://nlp.stanford.edu/IR-book/html/htmledition/stemming-and-lemmatization-1.html) - reducing words to common base forms
- Stop-word Removal - removing common words that carry little information
- "Vectorization" - convert text to a meainingful numeric vector representation (e.g. [term frequency encoding](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.CountVectorizer.html#sklearn.feature_extraction.text.CountVectorizer))

There are some commonly used libraries for the above tasks, we recommend [NLTK](https://www.nltk.org/) and [scikit-learn](https://scikit-learn.org/stable/).