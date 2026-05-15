"""CLI: Полибий."""

from cipher_suite.classical.polibiy import decrypt, encrypt

plainText = input("Шифруемый текст: ")
code = encrypt(plainText)
decode = decrypt(code)
print("Зашифровка:", code)
print("Расшифровка:", decode)
