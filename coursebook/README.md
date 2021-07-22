# Coursebook

We are using [jupyter-book](https://jupyterbook.org/intro.html) to develop our course. We will be using mix of markdown and jupyter notebook files, with binder providing a reproducible interactive computing environment. 

Course file structure:

```
coursebook/
    - figures/
    - modules/
        - m1/
            - files...
        - m2/
            - files...
        - m3/
            - files...
        - m4/
            - files...
    - _config.yml
    - _toc.yml
    requirement.txt
    welcome.md
```

To add a page:

- Add a markdown or jupyter notebook file to the corresponding module. You must have one top-level header (`#`), this will be the page link text in the book.
```
coursebook/
    - figures/
    - modules/
        - m1/
            - ethics_and_datascience.md
    ...
```

- Add the file to the table of contents `_toc.yml`. Do not include the file extension.
```
format: jb-book
root: welcome
parts:
  - caption: "Module 1: Introduction"
    chapters:
    - file: modules/m1/ethics_and_datascience
  - caption: "Module 2: Handling data and deployment"
  ...

```

- Test the build locally.
    - install `jupyter-book`. Recommended to use a fresh environment to avoid errors related to [package versions](https://github.com/executablebooks/jupyter-book/issues/1394). 
        - `pip install jupyter-book`; `conda install -c conda-forge jupyter-book`.
    - Build the book with `jupyter-book build coursebook`, this will generate html files in `coursebook/_build/html/`.
    - Inspect the book by opening `coursebook/_build/html/index.html` in your browser.
    - If you want to rebuild after changes, use `jupyter clean coursebook` to empty the `_build` directory.

- You don't need to commit the html files to github. When you push to `develop` the book will automatically be rebuilt, with the html pages deployed to `gh-pages`.
