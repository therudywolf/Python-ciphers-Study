"""ГОСТ Р 34.10-94 (учебная подпись): импорт и CLI."""

from cipher_suite.asymmetric.gost_34_10_94 import GOST_34_10_94_realisation

__all__ = ["GOST_34_10_94_realisation"]

if __name__ == "__main__":
    msg = input("Введите сообщение: ")
    out, chk = GOST_34_10_94_realisation(msg)
    print(out)
    print(chk)
