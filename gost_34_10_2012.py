"""ГОСТ Р 34.10-2012 (учебная подпись): импорт и CLI."""

from cipher_suite.asymmetric.gost_34_10_2012 import GOST_34_10_2012_realisation

__all__ = ["GOST_34_10_2012_realisation"]

if __name__ == "__main__":
    msg = input("Введите сообщение: ")
    out, chk = GOST_34_10_2012_realisation(msg.lower())
    print(out)
    print(chk)
