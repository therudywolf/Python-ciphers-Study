# Contributing to Python Cipher Suite

## Scope

This repository is an educational cryptography project. Keep changes focused, readable, and easy to run locally.

## Workflow

1. Create a branch for the change.
2. Make the smallest coherent change that solves the problem.
3. Run local checks before opening a pull request.
4. Verify that no personal files, editor state, tokens, or generated outputs are staged.

## Local checks

```bash
PYTHONDONTWRITEBYTECODE=1 python3 -m compileall -q GUI/*.py *.py
```

## Guidelines

- Write clear commit messages.
- Keep GUI changes usable on modest screen sizes.
- Prefer direct fixes over broad rewrites.
- Call out algorithm behavior changes explicitly in the description.
- Do not present this code as production-grade cryptography.

## Reporting issues

When reporting a bug, include the Python version, operating system, steps to reproduce, and the expected versus actual behavior.

## License

All contributions are licensed under the GNU Affero General Public License v3.0 or later.
