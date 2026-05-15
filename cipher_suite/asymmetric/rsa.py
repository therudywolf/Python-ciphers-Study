"""Учебная демонстрация RSA-подписи (не для production)."""

import random
from functools import lru_cache

from cipher_suite.constants import MESSAGE_ALPHABET


@lru_cache(maxsize=1)
def _primes_in_range() -> tuple:
    array = []
    for s in range(50, 1000):
        composite = False
        for i in range(2, s):
            if s % i == 0:
                composite = True
                break
        if not composite:
            array.append(s)
    return tuple(array)


def RSA_realisation(msg):
    final_otvet = ""
    final_check = ""
    array = list(_primes_in_range())
    final_otvet += "Простые числа (s):\n" + str(array) + "\n"

    p = int(random.choice(array))
    q = int(random.choice(array))
    final_otvet += "p = %d; q = %d\n" % (p, q)

    n = p * q
    Fn = (p - 1) * (q - 1)

    final_otvet += "n = %d; f(n) = %d\n" % (n, Fn)

    array2 = []
    for meow in range(2, 10000):
        d = int((1 + 2 * Fn) / meow)
        if d * meow == 1 + 2 * Fn:
            array2.append(meow)

    if not array2:
        raise ValueError("Невозможно найти взаимно простое число D для данных p и q.")

    final_otvet += "Подходящие для открытой экспоненты числа(D): " + str(array2) + "\n"

    D = int(random.choice(array2))

    final_otvet += "Открытая экспонента (D) =" + str(D) + "\n"

    k = 2

    E = int((1 + k * Fn) / D)

    final_otvet += "Секретная экспонента(E) =" + str(E) + "\n"

    if E * D != 1 + k * Fn:
        raise ValueError("Не удалось согласовать секретную экспоненту E с выбранным D.")

    public_key = [D, n]
    private_key = [E, n]

    final_otvet += "Публичный ключ: " + str(public_key) + "\n"
    final_otvet += "Приватный ключ: " + str(private_key) + "\n"

    alphavit = MESSAGE_ALPHABET

    msg_list = list(msg)
    alpha_code_msg = []
    for ch in msg_list:
        code = alphavit.get(ch)
        if code is None:
            continue
        alpha_code_msg.append(int(code))
    final_otvet += "Длина исходного сообщения {} символов".format(len(alpha_code_msg)) + "\n"

    def hash_value(n, _alpha_code):
        hashing_value = 1
        i = 0
        while i < len(alpha_code_msg):
            hashing_value = (((hashing_value - 1) + int(alpha_code_msg[i])) ** 2) % n
            i += 1
        return hashing_value

    hash_code_msg = hash_value(p, alpha_code_msg)
    final_otvet += "Хэш сообщения (m):= {}".format(hash_code_msg) + "\n"

    m = hash_code_msg

    Cm = pow(m, D, n)
    final_otvet += "Цифровая подпись (Cm): " + str(Cm) + "\n"

    Dm = pow(Cm, E, n)
    final_check += "Проверка цифровой подписи (Dm): " + str(Dm) + "\n"

    if m == Dm:
        final_check += str(m) + " = " + str(Dm) + "\n"
        final_check += "Подпись верна!" + "\n"
    else:
        final_check += str(m) + " != " + str(Dm) + "\n"
        final_check += "Подпись не верна!" + "\n"
    return final_otvet, final_check
