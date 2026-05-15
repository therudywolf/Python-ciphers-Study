"""CLI: вертикальная перестановка."""

from cipher_suite.classical.vertical import vertical_change

key = input("Введите ключ:")
msg = input("Введите текст:")
enc, dec = vertical_change(msg, key)
print("Зашифрованный текст:", enc)
print("Исходное сообщение (столбцы без ключа):", dec)
