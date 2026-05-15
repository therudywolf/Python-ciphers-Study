"""CLI: шифр Вернама."""

from cipher_suite.modern.vernam import notepad_shenona

msg = input("Введите текст: \n")
otvet = notepad_shenona(msg)
print(otvet[0])
print(otvet[1])
print(otvet[2])
print(otvet[3])
print(otvet[4])
