"""Современные и поточные шифры."""

from cipher_suite.modern.a5_first import a5_realisation
from cipher_suite.modern.a5_second import a52_realisation
from cipher_suite.modern.aes import AES_realize, run_aes_cli
from cipher_suite.modern.diffie_hellman import compute_shared_secret
from cipher_suite.modern.magma import Gamma, GammaOBR, imitovstavka, prZamena
from cipher_suite.modern.reshetka_kardano import reshetka_kardano
from cipher_suite.modern.vernam import notepad_shenona

__all__ = [
    "AES_realize",
    "Gamma",
    "GammaOBR",
    "a52_realisation",
    "a5_realisation",
    "compute_shared_secret",
    "imitovstavka",
    "notepad_shenona",
    "prZamena",
    "reshetka_kardano",
    "run_aes_cli",
]
