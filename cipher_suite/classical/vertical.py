"""Вертикальная перестановка."""

from typing import Dict


_ALPHABET_LOWER: Dict[str, int] = {
    "а": 0,
    "б": 1,
    "в": 2,
    "г": 3,
    "д": 4,
    "е": 5,
    "ж": 6,
    "з": 7,
    "и": 8,
    "й": 9,
    "к": 10,
    "л": 11,
    "м": 12,
    "н": 13,
    "о": 14,
    "п": 15,
    "р": 16,
    "с": 17,
    "т": 18,
    "у": 19,
    "ф": 20,
    "х": 21,
    "ц": 22,
    "ч": 23,
    "ш": 24,
    "щ": 25,
    "ъ": 26,
    "ы": 27,
    "ь": 28,
    "э": 29,
    "ю": 30,
    "я": 31,
    " ": 32,
    ",": 33,
    ".": 34,
    "А": 35,
    "Б": 36,
    "В": 37,
    "Г": 38,
    "Д": 39,
    "Е": 40,
    "Ж": 41,
    "З": 42,
    "И": 43,
    "Й": 44,
    "К": 45,
    "Л": 46,
    "М": 47,
    "Н": 48,
    "О": 49,
    "П": 50,
    "Р": 51,
    "С": 52,
    "Т": 53,
    "У": 54,
    "Ф": 55,
    "Х": 56,
    "Ц": 57,
    "Ч": 58,
    "Ш": 59,
    "Щ": 60,
    "Ъ": 61,
    "Ы": 62,
    "Ь": 63,
    "Э": 64,
    "Ю": 65,
    "Я": 66,
    "!": 67,
    "?": 68,
    ";": 69,
}


def vertical_change(text: str, key: str):
    key_len = len(key)
    msg = text
    while len(msg) < key_len * key_len:
        msg += "."
    msg_pl_key = key + msg
    list_msg = list(msg_pl_key)
    split_msg = [list_msg[i : i + key_len] for i in range(0, len(list_msg), key_len)]
    coded = []
    for row in split_msg:
        for cell in row:
            coded.append(_ALPHABET_LOWER.get(cell, 34))
    split_coded = [coded[i : i + key_len] for i in range(0, len(coded), key_len)]
    encrypted_matrix = []

    def sort_row(kl: int, badlist):
        k = key_len - 1
        while k > 0:
            ind = 0
            for j in range(k + 1):
                if badlist[0][j] > badlist[0][ind]:
                    ind = j
            for i in range(len(badlist)):
                tmp = badlist[i][ind]
                badlist[i][ind] = badlist[i][k]
                badlist[i][k] = tmp
            k -= 1
        for i in range(len(badlist)):
            for j in range(kl):
                encrypted_matrix.append(badlist[i][j])

    sort_row(key_len, split_coded)
    split_encrypted = [
        encrypted_matrix[i : i + key_len]
        for i in range(0, len(encrypted_matrix), key_len)
    ]

    def get_key(d: Dict[str, int], value):
        for k, v in d.items():
            if v == value:
                return k

    enc_result = ""
    for i in range(1, len(split_encrypted)):
        for j in range(len(split_encrypted[i])):
            ch = get_key(_ALPHABET_LOWER, split_encrypted[i][j])
            if ch:
                enc_result += ch

    dec_result = ""
    for i in range(1, len(split_msg)):
        for j in range(len(split_msg[i])):
            dec_result += split_msg[i][j]

    return enc_result, dec_result
