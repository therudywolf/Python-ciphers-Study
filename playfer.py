"""CLI: Плейфер."""

from cipher_suite.classical.playfair import playfer_crypt, playfer_decrypt

text = input(" Введите текст: ").lower()
key = input(" Введите ключ (без повторяющихся символов): ").lower()
enc = playfer_crypt(text, key)
dec = playfer_decrypt(enc, key)
print("Зашифровано:", enc)
print("Расшифровано:", dec)
