import tkinter as tk
from tkinter import messagebox, ttk
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from reshetka_kardano_final import reshetka_kardano
from re import findall
from vernam import notepad_shenona
from A5_first import a5_realisation
from A5_second import a52_realisation
from AES import AES_realize
from Magma import prZamena, Gamma, GammaOBR, imitovstavka
from RSA import RSA_realisation
from ElGamal import ElGamal_realisation
from GOST_34_10_94 import GOST_34_10_94_realisation
from GOST_34_10_2012 import GOST_34_10_2012_realisation


ALGORITHMS = [
    "Атбаш", "Цезарь", "Полибий", "Тритемий", "Белазо", "Виженер",
    "Матричный", "Плейфер", "Вертикальная перестановка",
    "Решётка Кардано", "Одноразовый блокнот Шеннона",
    "A5/1", "A5/2", "AES",
    "Магма (Простая замена)", "Магма (Гаммирование)",
    "Магма (Обратное гаммирование)", "Магма (Имитовставка)",
    "RSA", "El Gamal", "ГОСТ 34.10-94", "ГОСТ 34.10-2012"
]

ALGO_MAP = {name: idx + 1 for idx, name in enumerate(ALGORITHMS)}

DARK_BG = "#1e1e2e"
DARK_SURFACE = "#2d2d3f"
DARK_BORDER = "#3d3d5c"
ACCENT = "#7c3aed"
ACCENT_HOVER = "#6d28d9"
TEXT_PRIMARY = "#e2e8f0"
TEXT_SECONDARY = "#94a3b8"
SUCCESS = "#10b981"
ERROR = "#ef4444"

code = ''
decode = ''
key = ''
text = ''
krya = 0


# --- Cipher logic ---

def atbash_encrypt(text):
    alphavite = ',.!:\'\"#?@[](){} '
    result = ''
    for i in text:
        if i.isupper():
            k = ord(i) % ord('А')
            result += chr(ord('Я') - k)
        elif i.islower():
            k = ord(i) % ord('а')
            result += chr(ord('я') - k)
        else:
            if i in alphavite:
                result += alphavite[len(alphavite) - alphavite.find(i) - 1]
            else:
                result += i
    return result


def atbash_decrypt(text):
    return atbash_encrypt(text)


def cesar_encrypt(text, key):
    alphavite = ',.!:\'\"#?@[](){} '
    alphavite1 = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'
    alphavite2 = 'АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
    result = ""
    distance = int(key)
    for i in text:
        if i.islower():
            result += alphavite1[(alphavite1.find(i) + distance) % len(alphavite1)]
        elif i.isupper():
            result += alphavite2[(alphavite2.find(i) + distance) % len(alphavite2)]
        else:
            if i in alphavite:
                result += alphavite[(alphavite.find(i) + distance) % len(alphavite)]
            else:
                result += i
    return result


def cesar_decrypt(text, key):
    alphavite = ',.!:\'\"#?@[](){} '
    alphavite1 = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'
    alphavite2 = 'АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
    result = ""
    distance = int(key)
    for i in text:
        if i.islower():
            result += alphavite1[(alphavite1.find(i) - distance) % len(alphavite1)]
        elif i.isupper():
            result += alphavite2[(alphavite2.find(i) - distance) % len(alphavite2)]
        else:
            if i in alphavite:
                result += alphavite[(alphavite.find(i) - distance) % len(alphavite)]
            else:
                result += i
    return result


def polibiy_encrypt(text):
    alpha = 'абвгдежзийклмнопрстуфхцчшщъыьэюя, .!'
    result = ''
    text_lower = text.lower()
    for i in text_lower:
        pos = alpha.find(i)
        if pos >= 0:
            result += str(pos // 6 + 1) + str(pos % 6 + 1) + ' '
    return result.strip()


def polibiy_decrypt(text):
    alpha = 'абвгдежзийклмнопрстуфхцчшщъыьэюя, .!'
    parts = text.split()
    result = ''
    for i in parts:
        if len(i) >= 2:
            result += alpha[(int(i[0]) - 1) * 6 + int(i[1]) - 1]
    return result


def tritemiy_encrypt(text):
    alphavite = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'
    alphavite2 = alphavite.upper()
    alphavite3 = ',.!:\'\"#?@[](){} '
    result = ''
    meow = 0
    for i in text:
        if i.islower():
            result += alphavite[(alphavite.find(i) + meow) % len(alphavite)]
        elif i.isupper():
            result += alphavite2[(alphavite2.find(i) + meow) % len(alphavite2)]
        else:
            if i in alphavite3:
                result += alphavite3[(alphavite3.find(i) + meow) % len(alphavite3)]
            else:
                result += i
        meow += 1
    return result


def tritemiy_decrypt(text):
    alphavite = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'
    alphavite2 = alphavite.upper()
    alphavite3 = ',.!:\'\"#?@[](){} '
    result = ''
    meow = 0
    for i in text:
        if i.islower():
            result += alphavite[(alphavite.find(i) - meow) % len(alphavite)]
        elif i.isupper():
            result += alphavite2[(alphavite2.find(i) - meow) % len(alphavite2)]
        else:
            if i in alphavite3:
                result += alphavite3[(alphavite3.find(i) - meow) % len(alphavite3)]
            else:
                result += i
        meow += 1
    return result


def belazo_encrypt(text, key):
    alphavite = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'
    alphavite2 = alphavite.upper()
    alphavite3 = ',.!:\'\"#?@[](){} '
    result = ''
    meow = 0
    for i in text:
        if i.islower():
            result += alphavite[(alphavite.find(i) + alphavite.find(key[meow]) + 1) % len(alphavite)]
        elif i.isupper():
            result += alphavite2[(alphavite2.find(i) + alphavite2.find(key[meow].upper()) + 1) % len(alphavite2)]
        else:
            if i in alphavite3:
                result += alphavite3[(alphavite3.find(i) + alphavite3.find(key[meow]) - 1) % len(alphavite3)]
            else:
                result += i
        meow = (meow + 1) % len(key)
    return result


def belazo_decrypt(text, key):
    alphavite = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'
    alphavite2 = alphavite.upper()
    alphavite3 = ',.!:\'\"#?@[](){} '
    result = ''
    meow = 0
    for i in text:
        if i.islower():
            result += alphavite[(alphavite.find(i) - alphavite.find(key[meow]) - 1) % len(alphavite)]
        elif i.isupper():
            result += alphavite2[(alphavite2.find(i) - alphavite2.find(key[meow].upper()) - 1) % len(alphavite2)]
        else:
            if i in alphavite3:
                result += alphavite3[(alphavite3.find(i) - alphavite3.find(key[meow]) + 1) % len(alphavite3)]
            else:
                result += i
        meow = (meow + 1) % len(key)
    return result


def vigener_encrypt(text, key):
    alphavite = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'
    alphavite2 = alphavite.upper()
    alphavite3 = ',.!:\'\"#?@[](){} '
    result = ''
    full_key = key + text
    meow = 0
    for i in text:
        if i.islower():
            result += alphavite[(alphavite.find(i) + alphavite.find(full_key[meow])) % len(alphavite)]
        elif i.isupper():
            result += alphavite2[(alphavite2.find(i) + alphavite2.find(full_key[meow].upper())) % len(alphavite2)]
        else:
            if i in alphavite3:
                result += alphavite3[(alphavite3.find(i) + alphavite3.find(full_key[meow])) % len(alphavite3)]
            else:
                result += i
        meow = (meow + 1) % len(full_key)
    return result


def vigener_decrypt(text, key):
    alphavite = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'
    alphavite2 = alphavite.upper()
    alphavite3 = ',.!:\'\"#?@[](){} '
    full_key = key + text
    result = ''
    meow = 0
    for i in text:
        if i.islower():
            result += alphavite[(alphavite.find(i) - alphavite.find(full_key[meow])) % len(alphavite)]
        elif i.isupper():
            result += alphavite2[(alphavite2.find(i) - alphavite2.find(full_key[meow].upper())) % len(alphavite2)]
        else:
            if i in alphavite3:
                result += alphavite3[(alphavite3.find(i) - alphavite3.find(full_key[meow])) % len(alphavite3)]
            else:
                result += i
        meow = (meow + 1) % len(full_key)
    return result


# --- Matrix cipher helpers ---
alpha = tuple("АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ .,!/{}\'\"1234567890")
MatrixLength = 3
MatrixMod = len(alpha)
MatrixSquare = MatrixLength * MatrixLength
mainKey = ""


def checkErrors(key):
    if len(key) != MatrixSquare:
        return "Длина ключа не равна длине квадрата матрицы!"
    elif not getDeter(sliceto(key)):
        return "Определитель матрицы равен 0!"
    elif not getDeter(sliceto(key)) % MatrixMod:
        return "Определитель матрицы mod длина алфавита = 0"
    return None


def regular(text):
    template = r".{%d}" % MatrixLength
    return findall(template, text)


def encode(matrix):
    for x in range(len(matrix)):
        for y in range(MatrixLength):
            matrix[x][y] = alpha.index(matrix[x][y])
    return matrix


def decode_matrix(matrixM, matrixK, message=""):
    matrixF = []
    for z in range(len(matrixM)):
        temp = [0 for _ in range(MatrixLength)]
        for x in range(MatrixLength):
            for y in range(MatrixLength):
                temp[x] += matrixK[x][y] * matrixM[z][y]
            temp[x] = alpha[temp[x] % MatrixMod]
        matrixF.append(temp)
    for string in matrixF:
        message += "".join(string)
    return message


def sliceto(text):
    matrix = []
    for three in regular(text):
        matrix.append(list(three))
    return encode(matrix)


def iDet(det):
    for num in range(MatrixMod):
        if num * det % MatrixMod == 1:
            return num


def algebratic(x, y, det):
    global mainKey
    matrix = sliceto(mainKey)
    matrix.remove(matrix[x])
    for z in range(2):
        matrix[z].remove(matrix[z][y])
    det2x2 = matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    return (pow(-1, x + y) * det2x2 * iDet(det)) % MatrixMod


def getDeter(matrix):
    return (
        (matrix[0][0] * matrix[1][1] * matrix[2][2]) +
        (matrix[0][1] * matrix[1][2] * matrix[2][0]) +
        (matrix[1][0] * matrix[2][1] * matrix[0][2]) -
        (matrix[0][2] * matrix[1][1] * matrix[2][0]) -
        (matrix[0][1] * matrix[1][0] * matrix[2][2]) -
        (matrix[1][2] * matrix[2][1] * matrix[0][0])
    )


def getAlgbr(det, index=0):
    algbrs = [0 for _ in range(MatrixSquare)]
    for string in range(MatrixLength):
        for column in range(MatrixLength):
            algbrs[index] = algebratic(string, column, det)
            index += 1
    return algbrs


def getIMatr(algbr):
    return [
        [algbr[0], algbr[3], algbr[6]],
        [algbr[1], algbr[4], algbr[7]],
        [algbr[2], algbr[5], algbr[8]]
    ]


def encryptDecrypt(mode, message, key):
    MatrixMessage = sliceto(message)
    MatrixKey = sliceto(key)
    if mode == '1':
        return decode_matrix(MatrixMessage, MatrixKey)
    else:
        algbr = getAlgbr(getDeter(MatrixKey))
        return decode_matrix(MatrixMessage, getIMatr(algbr))


# --- Playfair cipher ---
def playfer_crypt(text, key):
    alphavite_lower = list('абвгдежзиклмнопрстуфхцчшщьыэюя')
    text = text.lower()
    for ch in list(text):
        if ch == ',':
            text = text.replace(ch, 'зпт')
        elif ch == ".":
            text = text.replace(ch, "тчк")
        elif ch not in alphavite_lower:
            text = text.replace(ch, '')
    new_alphabet = []
    for i in range(len(key)):
        if key[i] not in new_alphabet:
            new_alphabet.append(key[i])
    for ch in alphavite_lower:
        if ch not in new_alphabet:
            new_alphabet.append(ch)
    mtx = []
    counter = 0
    for j in range(5):
        row = []
        for i in range(6):
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
            enc_text += text[t:t+2]
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


def playfer_decrypt(text, key):
    alphavite_lower = list('абвгдежзиклмнопрстуфхцчшщьыэюя')
    text = text.lower()
    for ch in list(text):
        if ch not in alphavite_lower:
            text = text.replace(ch, '')
    new_alphabet = []
    for i in range(len(key)):
        if key[i] not in new_alphabet:
            new_alphabet.append(key[i])
    for ch in alphavite_lower:
        if ch not in new_alphabet:
            new_alphabet.append(ch)
    mtx = []
    counter = 0
    for j in range(5):
        row = []
        for i in range(6):
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
            enc_text += text[t:t+2]
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


# --- Vertical transposition ---
def vertical_change(text, key):
    alphabet_lower = {
        'а': 0, 'б': 1, 'в': 2, 'г': 3, 'д': 4, 'е': 5, 'ж': 6, 'з': 7,
        'и': 8, 'й': 9, 'к': 10, 'л': 11, 'м': 12, 'н': 13, 'о': 14, 'п': 15,
        'р': 16, 'с': 17, 'т': 18, 'у': 19, 'ф': 20, 'х': 21, 'ц': 22, 'ч': 23,
        'ш': 24, 'щ': 25, 'ъ': 26, 'ы': 27, 'ь': 28, 'э': 29, 'ю': 30, 'я': 31,
        ' ': 32, ",": 33, ".": 34, 'А': 35, 'Б': 36, 'В': 37, "Г": 38, "Д": 39,
        'Е': 40, 'Ж': 41, 'З': 42, 'И': 43, 'Й': 44, 'К': 45, 'Л': 46, 'М': 47,
        'Н': 48, 'О': 49, 'П': 50, 'Р': 51, 'С': 52, 'Т': 53, 'У': 54, 'Ф': 55,
        'Х': 56, 'Ц': 57, 'Ч': 58, 'Ш': 59, 'Щ': 60, 'Ъ': 61, 'Ы': 62, 'Ь': 63,
        'Э': 64, 'Ю': 65, 'Я': 66, '!': 67, "?": 68, ";": 69
    }
    key_len = len(key)
    msg = text
    while len(msg) < key_len * key_len:
        msg += '.'
    msg_pl_key = key + msg
    list_msg = list(msg_pl_key)
    split_msg = [list_msg[i:i + key_len] for i in range(0, len(list_msg), key_len)]
    coded = []
    for i in range(len(split_msg)):
        for j in range(len(split_msg[i])):
            val = alphabet_lower.get(split_msg[i][j], 34)
            coded.append(val)
    split_coded = [coded[i:i + key_len] for i in range(0, len(coded), key_len)]
    encrypted_matrix = []

    def sortRow(keylen, badlist):
        k = key_len - 1
        while k > 0:
            ind = 0
            for j in range(k + 1):
                if badlist[0][j] > badlist[0][ind]:
                    ind = j
            for i in range(len(badlist)):
                m = badlist[i][ind]
                badlist[i][ind] = badlist[i][k]
                badlist[i][k] = m
            k -= 1
        for i in range(len(badlist)):
            for j in range(keylen):
                encrypted_matrix.append(badlist[i][j])

    sortRow(key_len, split_coded)
    split_encrypted = [encrypted_matrix[i:i + key_len] for i in range(0, len(encrypted_matrix), key_len)]

    def get_key(d, value):
        for k, v in d.items():
            if v == value:
                return k

    enc_result = ''
    for i in range(1, len(split_encrypted)):
        for j in range(len(split_encrypted[i])):
            ch = get_key(alphabet_lower, split_encrypted[i][j])
            if ch:
                enc_result += ch

    dec_result = ""
    for i in range(1, len(split_msg)):
        for j in range(len(split_msg[i])):
            dec_result += split_msg[i][j]

    return enc_result, dec_result


# --- Main GUI Application ---
class CipherApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Python Cipher Suite")
        self.root.geometry("750x650")
        self.root.configure(bg=DARK_BG)
        self.root.minsize(700, 600)

        self.code = ''
        self.selected_algo = tk.StringVar(value=ALGORITHMS[0])
        self.result_var = tk.StringVar(value="")

        self._setup_styles()
        self._build_ui()

    def _setup_styles(self):
        style = ttk.Style()
        style.theme_use('clam')

        style.configure('TFrame', background=DARK_BG)
        style.configure('Surface.TFrame', background=DARK_SURFACE)
        style.configure('TLabel', background=DARK_BG, foreground=TEXT_PRIMARY, font=('Segoe UI', 10))
        style.configure('Title.TLabel', background=DARK_BG, foreground=TEXT_PRIMARY, font=('Segoe UI', 18, 'bold'))
        style.configure('Subtitle.TLabel', background=DARK_BG, foreground=TEXT_SECONDARY, font=('Segoe UI', 9))
        style.configure('Section.TLabel', background=DARK_SURFACE, foreground=TEXT_PRIMARY, font=('Segoe UI', 10, 'bold'))

        style.configure('TCombobox', fieldbackground=DARK_SURFACE, background=DARK_SURFACE,
                        foreground=TEXT_PRIMARY, selectbackground=ACCENT, borderwidth=1)
        style.map('TCombobox', fieldbackground=[('readonly', DARK_SURFACE)])

        style.configure('Accent.TButton', background=ACCENT, foreground='white',
                        font=('Segoe UI', 10, 'bold'), padding=(20, 10), borderwidth=0)
        style.map('Accent.TButton', background=[('active', ACCENT_HOVER)])

        style.configure('Secondary.TButton', background=DARK_BORDER, foreground=TEXT_PRIMARY,
                        font=('Segoe UI', 10), padding=(15, 8), borderwidth=0)
        style.map('Secondary.TButton', background=[('active', DARK_SURFACE)])

        style.configure('Success.TButton', background=SUCCESS, foreground='white',
                        font=('Segoe UI', 10, 'bold'), padding=(15, 8), borderwidth=0)

    def _build_ui(self):
        main_frame = ttk.Frame(self.root, style='TFrame', padding=20)
        main_frame.pack(fill=tk.BOTH, expand=True)

        # Header
        header = ttk.Frame(main_frame, style='TFrame')
        header.pack(fill=tk.X, pady=(0, 15))
        ttk.Label(header, text="Python Cipher Suite", style='Title.TLabel').pack(side=tk.LEFT)
        ttk.Label(header, text="v2.0 — Образовательный инструмент криптографии",
                  style='Subtitle.TLabel').pack(side=tk.LEFT, padx=(15, 0), pady=(8, 0))

        # Algorithm selection
        algo_frame = ttk.Frame(main_frame, style='TFrame')
        algo_frame.pack(fill=tk.X, pady=(0, 12))
        ttk.Label(algo_frame, text="Алгоритм:", style='TLabel').pack(side=tk.LEFT, padx=(0, 10))
        self.combo = ttk.Combobox(algo_frame, textvariable=self.selected_algo, values=ALGORITHMS,
                                  state='readonly', width=40, font=('Segoe UI', 10))
        self.combo.pack(side=tk.LEFT, fill=tk.X, expand=True)

        # Input fields
        input_frame = ttk.Frame(main_frame, style='TFrame')
        input_frame.pack(fill=tk.BOTH, expand=True, pady=(0, 12))

        # Text input
        text_label_frame = ttk.Frame(input_frame, style='TFrame')
        text_label_frame.pack(fill=tk.X, pady=(0, 4))
        ttk.Label(text_label_frame, text="Текст для обработки:", style='TLabel').pack(side=tk.LEFT)

        self.text_input = tk.Text(input_frame, height=5, bg=DARK_SURFACE, fg=TEXT_PRIMARY,
                                  insertbackground=TEXT_PRIMARY, font=('Consolas', 11),
                                  relief=tk.FLAT, borderwidth=0, padx=10, pady=8,
                                  selectbackground=ACCENT, wrap=tk.WORD)
        self.text_input.pack(fill=tk.X, pady=(0, 10))

        # Key input
        key_frame = ttk.Frame(input_frame, style='TFrame')
        key_frame.pack(fill=tk.X, pady=(0, 4))
        ttk.Label(key_frame, text="Ключ (если требуется):", style='TLabel').pack(side=tk.LEFT)

        self.key_input = tk.Entry(input_frame, bg=DARK_SURFACE, fg=TEXT_PRIMARY,
                                  insertbackground=TEXT_PRIMARY, font=('Consolas', 11),
                                  relief=tk.FLAT, borderwidth=0)
        self.key_input.pack(fill=tk.X, ipady=8, pady=(0, 15))

        # Buttons
        btn_frame = ttk.Frame(main_frame, style='TFrame')
        btn_frame.pack(fill=tk.X, pady=(0, 15))

        encrypt_btn = tk.Button(btn_frame, text="Зашифровать", bg=ACCENT, fg='white',
                                font=('Segoe UI', 11, 'bold'), relief=tk.FLAT, cursor='hand2',
                                activebackground=ACCENT_HOVER, activeforeground='white',
                                padx=25, pady=10, command=self._encrypt)
        encrypt_btn.pack(side=tk.LEFT, padx=(0, 10))

        decrypt_btn = tk.Button(btn_frame, text="Расшифровать", bg=DARK_BORDER, fg=TEXT_PRIMARY,
                                font=('Segoe UI', 11, 'bold'), relief=tk.FLAT, cursor='hand2',
                                activebackground=DARK_SURFACE, activeforeground=TEXT_PRIMARY,
                                padx=25, pady=10, command=self._decrypt)
        decrypt_btn.pack(side=tk.LEFT, padx=(0, 10))

        clear_btn = tk.Button(btn_frame, text="Очистить", bg=DARK_SURFACE, fg=TEXT_SECONDARY,
                              font=('Segoe UI', 10), relief=tk.FLAT, cursor='hand2',
                              activebackground=DARK_BORDER, activeforeground=TEXT_PRIMARY,
                              padx=15, pady=10, command=self._clear)
        clear_btn.pack(side=tk.LEFT, padx=(0, 10))

        dh_btn = tk.Button(btn_frame, text="Диффи-Хэллман", bg=DARK_SURFACE, fg=SUCCESS,
                           font=('Segoe UI', 10), relief=tk.FLAT, cursor='hand2',
                           activebackground=DARK_BORDER, activeforeground=SUCCESS,
                           padx=15, pady=10, command=self._open_diffie_hellman)
        dh_btn.pack(side=tk.RIGHT)

        # Result
        result_label_frame = ttk.Frame(main_frame, style='TFrame')
        result_label_frame.pack(fill=tk.X, pady=(0, 4))
        ttk.Label(result_label_frame, text="Результат:", style='TLabel').pack(side=tk.LEFT)

        self.result_output = tk.Text(main_frame, height=6, bg=DARK_SURFACE, fg=SUCCESS,
                                     font=('Consolas', 11), relief=tk.FLAT, borderwidth=0,
                                     padx=10, pady=8, wrap=tk.WORD, state=tk.DISABLED,
                                     selectbackground=ACCENT)
        self.result_output.pack(fill=tk.BOTH, expand=True)

    def _get_text(self):
        return self.text_input.get("1.0", tk.END).strip()

    def _get_key(self):
        return self.key_input.get().strip()

    def _show_result(self, text, is_error=False):
        self.result_output.config(state=tk.NORMAL)
        self.result_output.delete("1.0", tk.END)
        self.result_output.config(fg=ERROR if is_error else SUCCESS)
        self.result_output.insert("1.0", text)
        self.result_output.config(state=tk.DISABLED)

    def _encrypt(self):
        global mainKey
        algo = self.selected_algo.get()
        text = self._get_text()
        key = self._get_key()

        if not text:
            self._show_result("Введите текст для шифрования!", is_error=True)
            return

        try:
            if algo == "Атбаш":
                result = atbash_encrypt(text)
                self.code = result
                self._show_result(result)

            elif algo == "Цезарь":
                if not key:
                    self._show_result("Введите числовой ключ (дистанцию)!", is_error=True)
                    return
                result = cesar_encrypt(text, key)
                self.code = result
                self._show_result(result)

            elif algo == "Полибий":
                result = polibiy_encrypt(text)
                self.code = result
                self._show_result(result)

            elif algo == "Тритемий":
                result = tritemiy_encrypt(text)
                self.code = result
                self._show_result(result)

            elif algo == "Белазо":
                if not key:
                    self._show_result("Введите ключ!", is_error=True)
                    return
                result = belazo_encrypt(text, key)
                self.code = result
                self._show_result(result)

            elif algo == "Виженер":
                if not key:
                    self._show_result("Введите ключ!", is_error=True)
                    return
                result = vigener_encrypt(text, key)
                self.code = result
                self._show_result(result)

            elif algo == "Матричный":
                if not key or len(key.upper()) != 9:
                    self._show_result("Ключ должен быть длиной 9 символов!", is_error=True)
                    return
                mainKey = key.upper()
                err = checkErrors(mainKey)
                if err:
                    self._show_result(err, is_error=True)
                    return
                msg = text.upper()
                for s in msg:
                    if s not in alpha:
                        msg = msg.replace(s, '')
                while len(msg) % MatrixLength != 0:
                    msg += msg[-1]
                result = encryptDecrypt('1', msg, mainKey)
                self.code = result
                self._show_result(result)

            elif algo == "Плейфер":
                if not key:
                    self._show_result("Введите ключ!", is_error=True)
                    return
                result = playfer_crypt(text, key.lower())
                self.code = result
                self._show_result(result)

            elif algo == "Вертикальная перестановка":
                if not key:
                    self._show_result("Введите ключ!", is_error=True)
                    return
                enc, _ = vertical_change(text, key)
                self.code = enc
                self._show_result(enc)

            elif algo == "Решётка Кардано":
                if not key or not key.isdigit():
                    self._show_result("Введите размер матрицы (число)!", is_error=True)
                    return
                result = reshetka_kardano(int(key), text)
                self.code = result[0]
                self._show_result(result[0])

            elif algo == "Одноразовый блокнот Шеннона":
                result = notepad_shenona(text)
                self._show_result(result[0] + "\n" + result[1] + "\n" + result[2])

            elif algo == "A5/1":
                result = a5_realisation(text)
                self._show_result(result[0] + "\n" + result[1] + "\n" + result[2] + "\n" + result[3])

            elif algo == "A5/2":
                result = a52_realisation(text)
                self._show_result(result[0] + "\n" + result[1] + "\n" + result[2] + "\n" + result[3])

            elif algo == "AES":
                if not key:
                    self._show_result("Введите ключ (англ., до 16 символов)!", is_error=True)
                    return
                try:
                    os.remove("crypted_file.txt")
                except OSError:
                    pass
                with open('file.txt', 'w') as f:
                    f.write(text)
                AES_realize('1', key)
                with open("crypted_file.txt", 'r') as f2:
                    result = f2.read()
                self.code = result
                self._show_result(result)

            elif algo == "Магма (Простая замена)":
                result = prZamena(text)
                self._show_result("16-ричное сообщение:\n" + result[0] + "\nЗашифровано:\n" + result[1])

            elif algo == "Магма (Гаммирование)":
                result = Gamma(text)
                self._show_result("Дополненное сообщение:\n" + result[0] + "\nЗашифровано:\n" + result[1])

            elif algo == "Магма (Обратное гаммирование)":
                result = GammaOBR(text)
                self._show_result("Дополненное сообщение:\n" + result[0] + "\nЗашифровано:\n" + result[1])

            elif algo == "Магма (Имитовставка)":
                result = imitovstavka(text)
                self._show_result("16-ричное сообщение:\n" + result[0] + "\nИмитовставка:\n" + result[1])

            elif algo == "RSA":
                result = RSA_realisation(text)
                self._show_result("ЭЦП:\n" + result[0])
                self._rsa_result = result

            elif algo == "El Gamal":
                result = ElGamal_realisation(text)
                self._show_result("ЭЦП:\n" + result[0])
                self._elgamal_result = result

            elif algo == "ГОСТ 34.10-94":
                result = GOST_34_10_94_realisation(text)
                self._show_result("ЭЦП:\n" + result[0])
                self._gost94_result = result

            elif algo == "ГОСТ 34.10-2012":
                result = GOST_34_10_2012_realisation(text.lower())
                self._show_result("ЭЦП:\n" + result[0])
                self._gost2012_result = result

        except Exception as e:
            self._show_result(f"Ошибка: {str(e)}", is_error=True)

    def _decrypt(self):
        global mainKey
        algo = self.selected_algo.get()
        text = self._get_text()
        key = self._get_key()

        if not text and not self.code:
            self._show_result("Введите текст для расшифровки!", is_error=True)
            return

        try:
            if algo == "Атбаш":
                src = self.code if self.code else text
                result = atbash_decrypt(src)
                self._show_result(result)

            elif algo == "Цезарь":
                if not key:
                    self._show_result("Введите числовой ключ!", is_error=True)
                    return
                src = self.code if self.code else text
                result = cesar_decrypt(src, key)
                self._show_result(result)

            elif algo == "Полибий":
                src = self.code if self.code else text
                result = polibiy_decrypt(src)
                self._show_result(result)

            elif algo == "Тритемий":
                src = self.code if self.code else text
                result = tritemiy_decrypt(src)
                self._show_result(result)

            elif algo == "Белазо":
                if not key:
                    self._show_result("Введите ключ!", is_error=True)
                    return
                src = self.code if self.code else text
                result = belazo_decrypt(src, key)
                self._show_result(result)

            elif algo == "Виженер":
                if not key:
                    self._show_result("Введите ключ!", is_error=True)
                    return
                src = self.code if self.code else text
                result = vigener_decrypt(src, key)
                self._show_result(result)

            elif algo == "Матричный":
                if not key or len(key.upper()) != 9:
                    self._show_result("Ключ должен быть длиной 9 символов!", is_error=True)
                    return
                mainKey = key.upper()
                err = checkErrors(mainKey)
                if err:
                    self._show_result(err, is_error=True)
                    return
                src = self.code if self.code else text.upper()
                while len(src) % MatrixLength != 0:
                    src += src[-1]
                result = encryptDecrypt('2', src, mainKey)
                self._show_result(result)

            elif algo == "Плейфер":
                if not key:
                    self._show_result("Введите ключ!", is_error=True)
                    return
                src = self.code if self.code else text
                result = playfer_decrypt(src, key.lower())
                self._show_result(result)

            elif algo == "Вертикальная перестановка":
                if not key:
                    self._show_result("Введите ключ!", is_error=True)
                    return
                _, dec = vertical_change(text, key)
                self._show_result(dec)

            elif algo == "Решётка Кардано":
                if not key or not key.isdigit():
                    self._show_result("Введите размер матрицы (число)!", is_error=True)
                    return
                result = reshetka_kardano(int(key), text)
                self._show_result(result[1])

            elif algo == "Одноразовый блокнот Шеннона":
                result = notepad_shenona(text)
                self._show_result(result[3] + "\n" + result[4])

            elif algo == "A5/1":
                result = a5_realisation(text)
                self._show_result(result[4] + "\n" + result[5])

            elif algo == "A5/2":
                result = a52_realisation(text)
                self._show_result(result[4] + "\n" + result[5])

            elif algo == "AES":
                if not key:
                    self._show_result("Введите ключ!", is_error=True)
                    return
                try:
                    os.remove("decrypted_crypted_file.txt")
                except OSError:
                    pass
                AES_realize('2', key)
                with open("decrypted_crypted_file.txt", 'r') as f2:
                    result = f2.read()
                self._show_result(result)

            elif algo == "Магма (Простая замена)":
                result = prZamena(text)
                self._show_result("Расшифровано (16-рич):\n" + result[2] + "\nРасшифрованный текст:\n" + result[3])

            elif algo == "Магма (Гаммирование)":
                result = Gamma(text)
                self._show_result("Расшифрованное сообщение:\n" + result[2])

            elif algo == "Магма (Обратное гаммирование)":
                result = GammaOBR(text)
                self._show_result("Расшифрованное сообщение:\n" + result[2])

            elif algo == "Магма (Имитовставка)":
                self._show_result("Имитовставку нельзя расшифровать!", is_error=True)

            elif algo == "RSA":
                if hasattr(self, '_rsa_result'):
                    self._show_result("Проверка ЭЦП:\n" + self._rsa_result[1])
                else:
                    self._show_result("Сначала создайте ЭЦП (нажмите Зашифровать)!", is_error=True)

            elif algo == "El Gamal":
                if hasattr(self, '_elgamal_result'):
                    self._show_result("Проверка ЭЦП:\n" + self._elgamal_result[1])
                else:
                    self._show_result("Сначала создайте ЭЦП (нажмите Зашифровать)!", is_error=True)

            elif algo == "ГОСТ 34.10-94":
                if hasattr(self, '_gost94_result'):
                    self._show_result("Проверка ЭЦП:\n" + self._gost94_result[1])
                else:
                    self._show_result("Сначала создайте ЭЦП (нажмите Зашифровать)!", is_error=True)

            elif algo == "ГОСТ 34.10-2012":
                if hasattr(self, '_gost2012_result'):
                    self._show_result("Проверка ЭЦП:\n" + self._gost2012_result[1])
                else:
                    self._show_result("Сначала создайте ЭЦП (нажмите Зашифровать)!", is_error=True)

        except Exception as e:
            self._show_result(f"Ошибка: {str(e)}", is_error=True)

    def _clear(self):
        self.text_input.delete("1.0", tk.END)
        self.key_input.delete(0, tk.END)
        self.result_output.config(state=tk.NORMAL)
        self.result_output.delete("1.0", tk.END)
        self.result_output.config(state=tk.DISABLED)
        self.code = ''

    def _open_diffie_hellman(self):
        DiffieHellmanWindow(self.root)


class DiffieHellmanWindow(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Обмен ключами Диффи-Хэллмана")
        self.geometry("450x420")
        self.configure(bg=DARK_BG)
        self.resizable(False, False)
        self._build_ui()

    def _build_ui(self):
        frame = ttk.Frame(self, style='TFrame', padding=25)
        frame.pack(fill=tk.BOTH, expand=True)

        ttk.Label(frame, text="Диффи-Хэллман", style='Title.TLabel').pack(pady=(0, 5))
        ttk.Label(frame, text="Протокол обмена ключами", style='Subtitle.TLabel').pack(pady=(0, 20))

        fields = [
            ("Простое число P:", "p"),
            ("Натуральное число G:", "g"),
            ("Секретное число Алисы:", "ka"),
            ("Секретное число Боба:", "kb"),
        ]

        self.entries = {}
        for label_text, name in fields:
            row = ttk.Frame(frame, style='TFrame')
            row.pack(fill=tk.X, pady=5)
            ttk.Label(row, text=label_text, style='TLabel', width=25).pack(side=tk.LEFT)
            entry = tk.Entry(row, bg=DARK_SURFACE, fg=TEXT_PRIMARY, insertbackground=TEXT_PRIMARY,
                             font=('Consolas', 11), relief=tk.FLAT, width=15)
            entry.pack(side=tk.LEFT, fill=tk.X, expand=True, ipady=5)
            self.entries[name] = entry

        btn = tk.Button(frame, text="Обмен ключами", bg=SUCCESS, fg='white',
                        font=('Segoe UI', 11, 'bold'), relief=tk.FLAT, cursor='hand2',
                        activebackground='#059669', activeforeground='white',
                        padx=20, pady=10, command=self._exchange)
        btn.pack(pady=20)

        self.result_label = tk.Label(frame, text="", bg=DARK_BG, fg=TEXT_PRIMARY,
                                     font=('Consolas', 10), justify=tk.LEFT, wraplength=400)
        self.result_label.pack(fill=tk.X)

    def _exchange(self):
        try:
            p = int(self.entries['p'].get())
            g = int(self.entries['g'].get())
            ka = int(self.entries['ka'].get())
            kb = int(self.entries['kb'].get())

            if g ** (p - 1) % p != 1:
                messagebox.showinfo("Ошибка", "g^(p-1) mod p != 1\nВведите другие числа P и G!")
                return

            YA = g ** ka % p
            YB = g ** kb % p
            K1 = YB ** ka % p
            K2 = YA ** kb % p

            result = (
                f"Открытый ключ Алисы: {YA}\n"
                f"Открытый ключ Боба: {YB}\n"
                f"Общий секретный ключ: {K1}"
            )
            if K1 == K2:
                result += "\n\nКлючи совпали!"
            self.result_label.config(text=result, fg=SUCCESS)
        except ValueError:
            messagebox.showinfo("Ошибка", "Введите корректные числа!")
        except Exception as e:
            messagebox.showinfo("Ошибка", str(e))


if __name__ == "__main__":
    root = tk.Tk()
    app = CipherApp(root)
    root.mainloop()
