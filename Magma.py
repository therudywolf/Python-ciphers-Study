"""CLI: режимы Магмы."""

from cipher_suite.modern.magma import Gamma, GammaOBR, imitovstavka, prZamena

while True:
    message = input("Введите сообщение:\n")
    vibor = int(
        input(
            "Введите номер нужного режима:\n"
            "1. Простая замена\n2. Гаммирование\n"
            "3. Гаммирование с обратной связью\n4. Имитовставка\n"
        )
    )
    if vibor == 1:
        prZamena(message)
    if vibor == 2:
        Gamma(message)
    if vibor == 3:
        GammaOBR(message)
    if vibor == 4:
        imitovstavka(message)
