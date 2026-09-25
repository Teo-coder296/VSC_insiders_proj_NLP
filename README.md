# VSC Insiders NLP Project

A compact Python NLP text categorization project that reads labeled text samples, preprocesses them, trains a classifier, and predicts the category of new text using a repeatable and testable workflow.

## Overview

This project demonstrates a simple machine learning pipeline for text classification using:

- text normalization
- tokenization
- bag-of-words feature extraction
- logistic regression classification
- automated validation with pytest

## Project structure

```text
folder_gol/
├── README.md
├── main.py
├── requirements.txt
├── .gitignore
├── src/
│   ├── __init__.py
│   ├── preprocess.py
│   ├── features.py
│   ├── train.py
│   └── __init__.py
├── tests/
│   ├── test_preprocess.py
│   ├── test_features.py
│   └── test_model.py
└── LICENSE
```

## Run the example

```bash
python main.py
```

## Run tests

```bash
py -m pytest -q
```

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Author

Teo-coder296
