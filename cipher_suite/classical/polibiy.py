"""Квадрат Полибия (сетка 6 символов в строке)."""

ALPHA = "абвгдежзийклмнопрстуфхцчшщъыьэюя, .!"
WIDTH = 6


def encrypt(text: str) -> str:
    parts = []
    for ch in text.lower():
        pos = ALPHA.find(ch)
        if pos >= 0:
            parts.append(str(pos // WIDTH + 1) + str(pos % WIDTH + 1))
    return " ".join(parts)


def decrypt(text: str) -> str:
    parts_out = []
    for token in text.split():
        if len(token) >= 2:
            parts_out.append(ALPHA[(int(token[0]) - 1) * WIDTH + int(token[1]) - 1])
    return "".join(parts_out)
