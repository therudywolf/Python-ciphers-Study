"""CLI: учебная RSA-подпись."""

from cipher_suite.asymmetric.rsa import RSA_realisation


def main():
    msg = input("Введите сообщение: ")
    sig, check = RSA_realisation(msg)
    print(sig)
    print(check)


if __name__ == "__main__":
    main()
