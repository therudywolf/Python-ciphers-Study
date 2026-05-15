"""Обёртка для прежнего пути ``python "GOST 34.10-2012.py"``."""

from cipher_suite.asymmetric.gost_34_10_2012 import GOST_34_10_2012_realisation

if __name__ == "__main__":
    msg = input("Введите сообщение: ")
    out, chk = GOST_34_10_2012_realisation(msg.lower())
    print(out)
    print(chk)
