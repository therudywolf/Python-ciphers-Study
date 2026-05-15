"""Шифр Цезаря (кириллица + знаки из набора)."""

from typing import Union

from cipher_suite.text_utils import safe_index

PUNCT = ',.!:\'"#?@[](){} '
LOWER = "абвгдежзийклмнопрстуфхцчшщъыьэюя"
UPPER = LOWER.upper()


def encrypt(text: str, key: Union[str, int]) -> str:
    distance = int(key)
    parts = []
    for ch in text:
        if ch.islower():
            idx = safe_index(ch, LOWER)
            if idx is None:
                parts.append(ch)
            else:
                parts.append(LOWER[(idx + distance) % len(LOWER)])
        elif ch.isupper():
            idx = safe_index(ch, UPPER)
            if idx is None:
                parts.append(ch)
            else:
                parts.append(UPPER[(idx + distance) % len(UPPER)])
        else:
            idx = safe_index(ch, PUNCT)
            if idx is None:
                parts.append(ch)
            else:
                parts.append(PUNCT[(idx + distance) % len(PUNCT)])
    return "".join(parts)


def decrypt(text: str, key: Union[str, int]) -> str:
    distance = int(key)
    parts = []
    for ch in text:
        if ch.islower():
            idx = safe_index(ch, LOWER)
            if idx is None:
                parts.append(ch)
            else:
                parts.append(LOWER[(idx - distance) % len(LOWER)])
        elif ch.isupper():
            idx = safe_index(ch, UPPER)
            if idx is None:
                parts.append(ch)
            else:
                parts.append(UPPER[(idx - distance) % len(UPPER)])
        else:
            idx = safe_index(ch, PUNCT)
            if idx is None:
                parts.append(ch)
            else:
                parts.append(PUNCT[(idx - distance) % len(PUNCT)])
    return "".join(parts)
