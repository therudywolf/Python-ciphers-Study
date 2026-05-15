"""Шифр Белазо."""

from cipher_suite.text_utils import safe_index

LOWER = "абвгдежзийклмнопрстуфхцчшщъыьэюя"
UPPER = LOWER.upper()
PUNCT = ',.!:\'"#?@[](){} '


def encrypt(text: str, key: str) -> str:
    if not key:
        return text
    parts = []
    ki = 0
    for ch in text:
        kch = key[ki % len(key)]
        if ch.islower():
            ti = safe_index(ch, LOWER)
            kj = safe_index(kch, LOWER)
            if ti is None or kj is None:
                parts.append(ch)
            else:
                parts.append(LOWER[(ti + kj + 1) % len(LOWER)])
        elif ch.isupper():
            ti = safe_index(ch, UPPER)
            kj = safe_index(kch.upper(), UPPER)
            if ti is None or kj is None:
                parts.append(ch)
            else:
                parts.append(UPPER[(ti + kj + 1) % len(UPPER)])
        else:
            ti = safe_index(ch, PUNCT)
            kj = safe_index(kch, PUNCT)
            if ti is None or kj is None:
                parts.append(ch)
            else:
                parts.append(PUNCT[(ti + kj - 1) % len(PUNCT)])
        ki += 1
    return "".join(parts)


def decrypt(text: str, key: str) -> str:
    if not key:
        return text
    parts = []
    ki = 0
    for ch in text:
        kch = key[ki % len(key)]
        if ch.islower():
            ti = safe_index(ch, LOWER)
            kj = safe_index(kch, LOWER)
            if ti is None or kj is None:
                parts.append(ch)
            else:
                parts.append(LOWER[(ti - kj - 1) % len(LOWER)])
        elif ch.isupper():
            ti = safe_index(ch, UPPER)
            kj = safe_index(kch.upper(), UPPER)
            if ti is None or kj is None:
                parts.append(ch)
            else:
                parts.append(UPPER[(ti - kj - 1) % len(UPPER)])
        else:
            ti = safe_index(ch, PUNCT)
            kj = safe_index(kch, PUNCT)
            if ti is None or kj is None:
                parts.append(ch)
            else:
                parts.append(PUNCT[(ti - kj + 1) % len(PUNCT)])
        ki += 1
    return "".join(parts)
