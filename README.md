# VSC Insiders NLP Project

[![Python](https://img.shields.io/badge/Python-3.14-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![scikit-learn](https://img.shields.io/badge/scikit--learn-1.9-FFB300?logo=scikit-learn&logoColor=white)](https://scikit-learn.org/)
[![Pytest](https://img.shields.io/badge/Tests-pytest-0A9EDC?logo=pytest&logoColor=white)](https://pytest.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

A compact NLP text categorization project built in VS Code Insiders using Python, scikit-learn, and pytest. The project preprocesses labeled text samples, trains a lightweight classifier, and predicts the category of new text in a reproducible workflow.

## Overview

This project demonstrates a simple machine learning pipeline for text classification using:

- text normalization and cleaning
- tokenization for content analysis
- bag-of-words feature extraction
- logistic regression classification
- automated validation with pytest

## Features

- clean, modular Python project structure
- reusable preprocessing and feature-building modules
- trained classifier for short text classification
- test-driven development workflow
- easy local execution with a single script

## Quick start

```bash
python main.py
```

## Run tests

```bash
py -m pytest -q
```

## Project structure

```text
folder_gol/
├── README.md
├── LICENSE
├── main.py
├── requirements.txt
├── .gitignore
├── src/
│   ├── __init__.py
│   ├── preprocess.py
│   ├── features.py
│   ├── train.py
├── tests/
│   ├── test_preprocess.py
│   ├── test_features.py
│   └── test_model.py
└── .vscode/
```

## Example output

```text
finance
```

## Screenshots

Add a preview image here if you want to showcase the project UI or sample output.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Author

Teo-coder296
