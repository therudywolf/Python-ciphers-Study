"""CLI: Тритемий."""

from cipher_suite.classical.tritemius import decrypt, encrypt

plainText = input("Шифруемый текст: ")
code = encrypt(plainText)
decode = decrypt(code)
print("Зашифровка:", code)
print("Расшифровка:", decode)
