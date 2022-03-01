# Documentation
The API-documentation for this repo is generated from docstrings in the Python
source code, using the [Sphinx tool](https://www.sphinx-doc.org/).

## Generate documentation
Go to the docs-directory and run the following commands:
```shell
pipenv run sphinx-apidoc -o . ../ ../processing/tests ../dsf_situasjonsuttak/tests ../conftest.py ../familienummer/tests ../hendelses_uttrekk/tests ../search/tests ../quality/tests
pipenv run make html
```

Then open the `_build/html/index.html` file to view the documentation.
