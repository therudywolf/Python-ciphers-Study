"""CLI: матричный шифр (алфавит как в GUI)."""

from cipher_suite.classical.matrix import MatrixLength, alpha, check_errors, encrypt_decrypt

cryptMode = input(
    "Что будем делать? Введите цифру\n 1) Зашифровать\n 2) Расшифровать\n"
).strip()
if cryptMode not in ("1", "2"):
    print("Error: mode is not Found")
    raise SystemExit

startMessage = input("Введите текст: ").upper()
mainKey = input("Введите ключ: ").upper()

err = check_errors(mainKey)
if err:
    print(err)
    raise SystemExit

for symbol in list(startMessage):
    if symbol not in alpha:
        startMessage = startMessage.replace(symbol, "")

while len(startMessage) % MatrixLength != 0:
    startMessage += startMessage[-1]

print("Final message:", encrypt_decrypt(cryptMode, startMessage, mainKey))
