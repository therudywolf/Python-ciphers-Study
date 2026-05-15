"""Безопасная работа с позициями символов в алфавите."""

from typing import Optional


def safe_index(char: str, alphabet: str) -> Optional[int]:
    if len(char) != 1:
        return None
    pos = alphabet.find(char)
    return None if pos < 0 else pos
