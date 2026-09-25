from typing import Sequence, Tuple

import numpy as np
from sklearn.feature_extraction.text import CountVectorizer


def build_feature_matrix(documents: Sequence[str]) -> Tuple[np.ndarray, list[str]]:
    if documents is None or len(documents) == 0:
        raise ValueError("documents cannot be empty")

    vectorizer = CountVectorizer()
    matrix = vectorizer.fit_transform(documents)
    return matrix.toarray(), vectorizer.get_feature_names_out().tolist()


def validate_feature_matrix(matrix: Sequence[Sequence[float]]) -> np.ndarray:
    if matrix is None or len(matrix) == 0:
        raise ValueError("feature matrix cannot be empty")

    array = np.asarray(matrix)
    if array.size == 0:
        raise ValueError("feature matrix cannot be empty")
    return array
