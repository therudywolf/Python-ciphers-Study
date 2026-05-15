"""CLI: учебная подпись Эль-Гамаля."""

from cipher_suite.asymmetric.elgamal import ElGamal_realisation


def main():
    msg = input("Введите сообщение:")
    out = ElGamal_realisation(msg)
    print(out[0], "\n" + out[1])


if __name__ == "__main__":
    main()
