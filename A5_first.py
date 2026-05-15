"""CLI: A5/1."""

from cipher_suite.modern.a5_first import a5_realisation

s = input("Введите сообщение:\n")
otvet = a5_realisation(s)
print(otvet[0])
print(otvet[1])
print(otvet[2])
print(otvet[3])
print(otvet[4])
print(otvet[5])
