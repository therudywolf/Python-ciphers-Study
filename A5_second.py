"""CLI: A5/2."""

from cipher_suite.modern.a5_second import a52_realisation

s = input("Введите сообщение:\n")
otvet = a52_realisation(s)
print(otvet[0])
print(otvet[1])
print(otvet[2])
print(otvet[3])
print(otvet[4])
print(otvet[5])
