"""Совместимость с именем файла ``diffie-hellman.py`` (дефис в имени).

Рекомендуется: python diffie_hellman.py
"""

from cipher_suite.modern.diffie_hellman import compute_shared_secret


def main():
    p = int(input("Введите простое число P: "))
    g = int(input("Введите натуральное число G: "))
    ka = int(input("Введите натуральное (секретное) число Алисы - kа: "))
    kb = int(input("Введите натуральное (секретное) число Боба - kb: "))
    YA, YB, K1, K2 = compute_shared_secret(p, g, ka, kb)
    print("Открытый ключ Алисы: ", YA, "\nОткрытый ключ Боба: ", YB)
    print("Приватный ключ Алисы: ", K1, "\nПриватный ключ Боба: ", K2)


if __name__ == "__main__":
    main()
