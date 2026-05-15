"""CLI: решётка Кардано."""

from cipher_suite.modern.reshetka_kardano import reshetka_kardano

SIZE = int(input(" Введите размер матрицы (одно число): "))
text = input(" Введите текст: ")
encrypted_text, decrypted_text = reshetka_kardano(SIZE, text)
print(encrypted_text, decrypted_text)
