"""CLI: Виженер."""

from cipher_suite.classical.vigener import decrypt, encrypt

plainText = input("Шифруемый текст: ")
key = input("Введите ключ: ")
code = encrypt(plainText, key)
decode = decrypt(code, key)
print("Зашифровка:", code)
print("Расшифровка:", decode)
