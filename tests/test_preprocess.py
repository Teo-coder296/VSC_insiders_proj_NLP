from src.preprocess import normalize_text, tokenize


def test_normalize_text_lowercases_and_removes_punctuation():
    text = "  BREAKING NEWS: AI is HERE!!!  "
    result = normalize_text(text)
    assert result == "breaking news ai is here"


def test_tokenize_splits_and_drops_empty_strings():
    text = "Machine learning helps teams classify text quickly."
    result = tokenize(text)
    assert result == [
        "machine",
        "learning",
        "helps",
        "teams",
        "classify",
        "text",
        "quickly",
    ]
