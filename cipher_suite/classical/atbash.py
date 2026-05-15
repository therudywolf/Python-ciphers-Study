"""Атбаш для кириллицы и набора знаков препинания."""

PUNCT = ',.!:\'"#?@[](){} '


def encrypt(text: str) -> str:
    parts = []
    for ch in text:
        if ch.isupper():
            k = ord(ch) % ord("А")
            parts.append(chr(ord("Я") - k))
        elif ch.islower():
            k = ord(ch) % ord("а")
            parts.append(chr(ord("я") - k))
        else:
            idx = PUNCT.find(ch)
            if idx >= 0:
                parts.append(PUNCT[len(PUNCT) - idx - 1])
            else:
                parts.append(ch)
    return "".join(parts)


def decrypt(text: str) -> str:
    return encrypt(text)
