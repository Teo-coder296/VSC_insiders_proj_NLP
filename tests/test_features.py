import numpy as np

from src.features import build_feature_matrix, validate_feature_matrix


def test_build_feature_matrix_returns_dense_array():
    documents = ["market gains after earnings", "stock prices rise today"]
    matrix, vocabulary = build_feature_matrix(documents)

    assert isinstance(matrix, np.ndarray)
    assert matrix.shape[0] == 2
    assert len(vocabulary) > 0
    assert matrix.sum() > 0


def test_validate_feature_matrix_rejects_empty_input():
    try:
        validate_feature_matrix([])
        assert False, "Expected ValueError for empty feature matrix"
    except ValueError:
        pass
