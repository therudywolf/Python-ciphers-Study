# Contributing

## Scope

This repository is an educational cryptography project. Keep changes focused, readable, and easy to run locally.

## Before opening a change

1. Run `PYTHONDONTWRITEBYTECODE=1 python3 -m compileall -q GUI/*.py *.py`
2. Check that no personal files, editor state, tokens, or generated outputs are staged
3. Keep algorithm behavior changes explicit in the description

## Style

- Prefer small, direct fixes over broad rewrites
- Keep GUI changes usable on modest screen sizes
- Avoid committing generated text outputs and local IDE configuration

## Security

Do not present this code as production-grade cryptography. If a change touches key handling, signatures, or randomness, call that out clearly in the review notes.
