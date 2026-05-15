"""Шифр Тритемия."""

from cipher_suite.text_utils import safe_index

LOWER = "абвгдежзийклмнопрстуфхцчшщъыьэюя"
UPPER = LOWER.upper()
PUNCT = ',.!:\'"#?@[](){} '


def encrypt(text: str) -> str:
    parts = []
    step = 0
    for ch in text:
        if ch.islower():
            idx = safe_index(ch, LOWER)
            if idx is None:
                parts.append(ch)
            else:
                parts.append(LOWER[(idx + step) % len(LOWER)])
        elif ch.isupper():
            idx = safe_index(ch, UPPER)
            if idx is None:
                parts.append(ch)
            else:
                parts.append(UPPER[(idx + step) % len(UPPER)])
        else:
            idx = safe_index(ch, PUNCT)
            if idx is None:
                parts.append(ch)
            else:
                parts.append(PUNCT[(idx + step) % len(PUNCT)])
        step += 1
    return "".join(parts)


def decrypt(text: str) -> str:
    parts = []
    step = 0
    for ch in text:
        if ch.islower():
            idx = safe_index(ch, LOWER)
            if idx is None:
                parts.append(ch)
            else:
                parts.append(LOWER[(idx - step) % len(LOWER)])
        elif ch.isupper():
            idx = safe_index(ch, UPPER)
            if idx is None:
                parts.append(ch)
            else:
                parts.append(UPPER[(idx - step) % len(UPPER)])
        else:
            idx = safe_index(ch, PUNCT)
            if idx is None:
                parts.append(ch)
            else:
                parts.append(PUNCT[(idx - step) % len(PUNCT)])
        step += 1
    return "".join(parts)
