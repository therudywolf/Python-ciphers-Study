"""Обмен ключами Диффи–Хеллмана (учебная формула)."""


def compute_shared_secret(p: int, g: int, ka: int, kb: int):
    if pow(g, p - 1, p) != 1:
        raise ValueError("Условие протокола: ожидается g^(p-1) mod p == 1.")
    ya = pow(g, ka, p)
    yb = pow(g, kb, p)
    k1 = pow(yb, ka, p)
    k2 = pow(ya, kb, p)
    return ya, yb, k1, k2
