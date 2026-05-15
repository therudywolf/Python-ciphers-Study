"""Шифр Виженера (ключ дополняется открытым текстом)."""

from cipher_suite.text_utils import safe_index

LOWER = "абвгдежзийклмнопрстуфхцчшщъыьэюя"
UPPER = LOWER.upper()
PUNCT = ',.!:\'"#?@[](){} '


def encrypt(text: str, key: str) -> str:
    if not key:
        return text
    full_key = key + text
    fk_len = len(full_key)
    parts = []
    mi = 0
    for ch in text:
        fk = full_key[mi % fk_len]
        if ch.islower():
            ti = safe_index(ch, LOWER)
            fi = safe_index(fk, LOWER)
            if ti is None or fi is None:
                parts.append(ch)
            else:
                parts.append(LOWER[(ti + fi) % len(LOWER)])
        elif ch.isupper():
            ti = safe_index(ch, UPPER)
            fi = safe_index(fk.upper(), UPPER)
            if ti is None or fi is None:
                parts.append(ch)
            else:
                parts.append(UPPER[(ti + fi) % len(UPPER)])
        else:
            ti = safe_index(ch, PUNCT)
            fi = safe_index(fk, PUNCT)
            if ti is None or fi is None:
                parts.append(ch)
            else:
                parts.append(PUNCT[(ti + fi) % len(PUNCT)])
        mi += 1
    return "".join(parts)


def decrypt(text: str, key: str) -> str:
    if not key:
        return text
    full_key = key + text
    fk_len = len(full_key)
    parts = []
    mi = 0
    for ch in text:
        fk = full_key[mi % fk_len]
        if ch.islower():
            ti = safe_index(ch, LOWER)
            fi = safe_index(fk, LOWER)
            if ti is None or fi is None:
                parts.append(ch)
            else:
                parts.append(LOWER[(ti - fi) % len(LOWER)])
        elif ch.isupper():
            ti = safe_index(ch, UPPER)
            fi = safe_index(fk.upper(), UPPER)
            if ti is None or fi is None:
                parts.append(ch)
            else:
                parts.append(UPPER[(ti - fi) % len(UPPER)])
        else:
            ti = safe_index(ch, PUNCT)
            fi = safe_index(fk, PUNCT)
            if ti is None or fi is None:
                parts.append(ch)
            else:
                parts.append(PUNCT[(ti - fi) % len(PUNCT)])
        mi += 1
    return "".join(parts)
