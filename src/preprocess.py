import re
from typing import List


def normalize_text(text: str) -> str:
    if text is None:
        raise ValueError("Text input cannot be None.")

    normalized = text.lower()
    normalized = re.sub(r"[^a-z0-9\s]", " ", normalized)
    normalized = re.sub(r"\s+", " ", normalized).strip()
    return normalized


def tokenize(text: str) -> List[str]:
    cleaned = normalize_text(text)
    return [token for token in re.findall(r"[a-z0-9]+", cleaned) if token]
