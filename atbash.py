"""CLI: атбаш."""

from cipher_suite.classical.atbash import decrypt, encrypt

text = input("Введите открытый текст: ")
code = encrypt(text)
text_decode = code if code else text
decode = decrypt(text_decode)
print("Зашифровка:", code)
print("Расшифровка:", decode)
