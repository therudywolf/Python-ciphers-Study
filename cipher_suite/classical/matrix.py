"""Матричный шифр Хилла 3×3 по расширенному алфавиту."""

from re import findall

ALPHA = tuple("АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ .,!/{}\'\"1234567890")
alpha = ALPHA
MatrixLength = 3
MatrixMod = len(ALPHA)
MatrixSquare = MatrixLength * MatrixLength


def check_errors(key: str):
    if len(key) != MatrixSquare:
        return "Длина ключа не равна длине квадрата матрицы!"
    det = get_deter(sliceto(key))
    if not det:
        return "Определитель матрицы равен 0!"
    if not det % MatrixMod:
        return "Определитель матрицы mod длина алфавита = 0"
    return None


checkErrors = check_errors


def regular(text):
    template = r".{%d}" % MatrixLength
    return findall(template, text)


def encode(matrix):
    for x in range(len(matrix)):
        for y in range(MatrixLength):
            matrix[x][y] = ALPHA.index(matrix[x][y])
    return matrix


def decode_matrix(matrixM, matrixK):
    rows = []
    for z in range(len(matrixM)):
        temp = [0 for _ in range(MatrixLength)]
        for x in range(MatrixLength):
            for y in range(MatrixLength):
                temp[x] += matrixK[x][y] * matrixM[z][y]
            temp[x] = ALPHA[temp[x] % MatrixMod]
        rows.append("".join(temp))
    return "".join(rows)


def sliceto(text):
    matrix = []
    for three in regular(text):
        matrix.append(list(three))
    return encode(matrix)


def i_det(det):
    for num in range(MatrixMod):
        if num * det % MatrixMod == 1:
            return num
    return None


def algebratic(x, y, det, key_str: str):
    matrix = [row[:] for row in sliceto(key_str)]
    matrix.pop(x)
    for z in range(2):
        matrix[z].pop(y)
    det2x2 = matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    inv = i_det(det)
    if inv is None:
        return 0
    return (pow(-1, x + y) * det2x2 * inv) % MatrixMod


def get_deter(matrix):
    return (
        (matrix[0][0] * matrix[1][1] * matrix[2][2])
        + (matrix[0][1] * matrix[1][2] * matrix[2][0])
        + (matrix[1][0] * matrix[2][1] * matrix[0][2])
        - (matrix[0][2] * matrix[1][1] * matrix[2][0])
        - (matrix[0][1] * matrix[1][0] * matrix[2][2])
        - (matrix[1][2] * matrix[2][1] * matrix[0][0])
    )


def get_algbr(det, key_str: str, index=0):
    algbrs = [0 for _ in range(MatrixSquare)]
    for string in range(MatrixLength):
        for column in range(MatrixLength):
            algbrs[index] = algebratic(string, column, det, key_str)
            index += 1
    return algbrs


def get_inv_matr(algbr):
    return [
        [algbr[0], algbr[3], algbr[6]],
        [algbr[1], algbr[4], algbr[7]],
        [algbr[2], algbr[5], algbr[8]],
    ]


def encrypt_decrypt(mode, message, key):
    key_u = key.upper()
    matrix_message = sliceto(message)
    matrix_key = sliceto(key_u)
    if mode == "1":
        return decode_matrix(matrix_message, matrix_key)
    algbr = get_algbr(get_deter(matrix_key), key_u)
    return decode_matrix(matrix_message, get_inv_matr(algbr))


encryptDecrypt = encrypt_decrypt
