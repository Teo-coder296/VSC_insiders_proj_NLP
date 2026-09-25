from __future__ import annotations

from typing import Sequence

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline

from src.preprocess import tokenize


def train_classifier(documents: Sequence[str], labels: Sequence[str]) -> Pipeline:
    if len(documents) != len(labels):
        raise ValueError("documents and labels must have the same length")
    if not documents:
        raise ValueError("documents cannot be empty")

    model = Pipeline(
        steps=[
            ("vectorizer", CountVectorizer(tokenizer=tokenize)),
            ("classifier", LogisticRegression(max_iter=1000)),
        ]
    )
    model.fit(documents, labels)
    return model


def predict_label(classifier: Pipeline, text: str) -> str:
    if classifier is None:
        raise ValueError("classifier cannot be None")
    if text is None:
        raise ValueError("text cannot be None")

    prediction = classifier.predict([text])
    return prediction[0]
