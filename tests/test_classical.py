"""Регрессионные тесты классических шифров."""

from cipher_suite.classical.atbash import decrypt as atbash_decrypt, encrypt as atbash_encrypt
from cipher_suite.classical.belazo import decrypt as belazo_decrypt, encrypt as belazo_encrypt
from cipher_suite.classical.caesar import decrypt as caesar_decrypt, encrypt as caesar_encrypt
from cipher_suite.classical.polibiy import decrypt as polibiy_decrypt, encrypt as polibiy_encrypt
from cipher_suite.classical.tritemius import decrypt as tritemius_decrypt, encrypt as tritemius_encrypt
from cipher_suite.classical.vertical import vertical_change
from cipher_suite.classical.vigener import decrypt as vigener_decrypt, encrypt as vigener_encrypt
from cipher_suite.modern.diffie_hellman import compute_shared_secret


def test_caesar_roundtrip_cyrillic():
    text = "абв"
    assert caesar_decrypt(caesar_encrypt(text, 3), 3) == text


def test_caesar_latin_passthrough():
    out = caesar_encrypt("aб", 1)
    assert out[0] == "a"


def test_atbash_roundtrip():
    s = "Абв"
    assert atbash_decrypt(atbash_encrypt(s)) == s


def test_polibiy_roundtrip():
    s = "аб"
    assert polibiy_decrypt(polibiy_encrypt(s)) == s


def test_tritemius_preserves_unknown():
    out = tritemius_encrypt("xаб")
    assert out[0] == "x"


def test_belazo_requires_valid_key_chars_for_shift():
    msg = "аб"
    key = "аб"
    assert belazo_decrypt(belazo_encrypt(msg, key), key) == msg


def test_vigener_roundtrip():
    msg = "абв"
    key = "ключ"
    assert vigener_decrypt(vigener_encrypt(msg, key), key) == msg


def test_vertical_change_returns_strings():
    enc, dec = vertical_change("привет", "ключ")
    assert isinstance(enc, str)
    assert isinstance(dec, str)


def test_diffie_hellman_shared_secret():
    p, g, ka, kb = 7, 3, 2, 4
    ya, yb, k1, k2 = compute_shared_secret(p, g, ka, kb)
    assert k1 == k2
    assert ya == pow(g, ka, p)
