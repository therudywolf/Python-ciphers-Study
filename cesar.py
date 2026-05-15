"""CLI: Цезарь."""

from cipher_suite.classical.caesar import decrypt, encrypt

plainText = input("Шифруемый текст: ")
distance = int(input("Дистанция: "))
code = encrypt(plainText, distance)
decode = decrypt(code, distance)
print("Зашифровка:", code)
print("Расшифровка:", decode)
