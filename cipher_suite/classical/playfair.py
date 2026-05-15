"""Шифр Плейфера (учебная решётка 5×6)."""


def playfer_crypt(text: str, key: str) -> str:
    alphavite_lower = list("абвгдежзиклмнопрстуфхцчшщьыэюя")
    text = text.lower()
    for ch in list(text):
        if ch == ",":
            text = text.replace(ch, "зпт")
        elif ch == ".":
            text = text.replace(ch, "тчк")
        elif ch not in alphavite_lower:
            text = text.replace(ch, "")
    new_alphabet = []
    for ch in key:
        if ch not in new_alphabet:
            new_alphabet.append(ch)
    for ch in alphavite_lower:
        if ch not in new_alphabet:
            new_alphabet.append(ch)
    mtx = []
    counter = 0
    for _j in range(5):
        row = []
        for _i in range(6):
            row.append(new_alphabet[counter])
            counter += 1
        mtx.append(row)
    if len(text) % 2 == 1:
        text += "я"
    enc_text = ""
    for t in range(0, len(text), 2):
        j1, i1, j2, i2 = -1, -1, -1, -1
        for j in range(5):
            for i in range(6):
                if mtx[j][i] == text[t]:
                    j1, i1 = j, i
                if mtx[j][i] == text[t + 1]:
                    j2, i2 = j, i
        if j1 == -1 or j2 == -1:
            enc_text += text[t : t + 2]
            continue
        if j1 != j2 and i1 != i2:
            enc_text += mtx[j1][i2] + mtx[j2][i1]
        elif j1 == j2 and i1 != i2:
            enc_text += mtx[j1][(i1 + 1) % 6] + mtx[j2][(i2 + 1) % 6]
        elif j1 != j2 and i1 == i2:
            enc_text += mtx[(j1 - 1) % 5][i1] + mtx[(j2 - 1) % 5][i2]
        else:
            enc_text += mtx[j1][i1] + mtx[j1][i1]
    return enc_text


def playfer_decrypt(text: str, key: str) -> str:
    alphavite_lower = list("абвгдежзиклмнопрстуфхцчшщьыэюя")
    text = text.lower()
    for ch in list(text):
        if ch not in alphavite_lower:
            text = text.replace(ch, "")
    new_alphabet = []
    for ch in key:
        if ch not in new_alphabet:
            new_alphabet.append(ch)
    for ch in alphavite_lower:
        if ch not in new_alphabet:
            new_alphabet.append(ch)
    mtx = []
    counter = 0
    for _j in range(5):
        row = []
        for _i in range(6):
            row.append(new_alphabet[counter])
            counter += 1
        mtx.append(row)
    if len(text) % 2 == 1:
        text += "я"
    enc_text = ""
    for t in range(0, len(text), 2):
        j1, i1, j2, i2 = -1, -1, -1, -1
        for j in range(5):
            for i in range(6):
                if mtx[j][i] == text[t]:
                    j1, i1 = j, i
                if mtx[j][i] == text[t + 1]:
                    j2, i2 = j, i
        if j1 == -1 or j2 == -1:
            enc_text += text[t : t + 2]
            continue
        if j1 != j2 and i1 != i2:
            enc_text += mtx[j1][i2] + mtx[j2][i1]
        elif j1 == j2 and i1 != i2:
            enc_text += mtx[j1][(i1 - 1) % 6] + mtx[j2][(i2 - 1) % 6]
        elif j1 != j2 and i1 == i2:
            enc_text += mtx[(j1 + 1) % 5][i1] + mtx[(j2 + 1) % 5][i2]
        else:
            enc_text += mtx[j1][i1] + mtx[j1][i1]
    return enc_text
