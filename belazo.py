"""CLI: Белазо."""

from cipher_suite.classical.belazo import decrypt, encrypt

text = input("Введите сообщение \n")
key = input("Введите ключ \n")
code = encrypt(text, key)
print(code)
print(decrypt(code, key))
