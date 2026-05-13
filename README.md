# Python Cipher Suite

This project is licensed under the GNU Affero General Public License v3.0 or later.

> Образовательный инструмент, включающий десятки классических и современных криптографических алгоритмов. Реализован в виде CLI- и GUI-приложений на Python.

## Поддерживаемые алгоритмы

### Классические

| Алгоритм | CLI | GUI |
|----------|-----|-----|
| Атбаш | `atbash.py` | + |
| Цезарь | `cesar.py` | + |
| Полибий | `polibiy.py` | + |
| Тритемий | `tritemiy.py` | + |
| Белазо | `belazo.py` | + |
| Виженер | `vigener.py` | + |
| Плейфер | `playfer.py` | + |
| Вертикальная перестановка | `vertical_change.py` | + |
| Матричный шифр | `matrichniy.py` | + |
| Решётка Кардано | `reshetka_kardano_final.py` | + |

### Симметричные (современные)

| Алгоритм | CLI | GUI |
|----------|-----|-----|
| AES-128 | `AES.py` | + |
| Магма (замена, гамма, имитовставка) | `Magma.py` | + |
| Шифр Вернама (одноразовый блокнот) | `vernam.py` | + |
| A5/1 | `A5_first.py` | + |
| A5/2 | `A5_second.py` | + |

### Асимметричные (ЭЦП)

| Алгоритм | CLI | GUI |
|----------|-----|-----|
| RSA | `RSA.py` | + |
| ElGamal | `ElGamal.py` | + |
| ГОСТ 34.10-94 | `GOST 34.10-94.py` | + |
| ГОСТ 34.10-2012 | `GOST 34.10-2012.py` | + |

### Обмен ключами

| Алгоритм | CLI | GUI |
|----------|-----|-----|
| Диффи-Хэллман | `diffie-hellman.py` | + |

## Быстрый запуск

### Запуск GUI

```bash
python GUI/Visual_Algorithms_final.py
```

### Запуск CLI-алгоритма

```bash
python cesar.py
python RSA.py
python Magma.py
```

## Запуск через Docker

```bash
# Сборка образа
docker build -t python-cipher .

# Запуск (Linux с X11)
docker run -it --rm -e DISPLAY=$DISPLAY -v /tmp/.X11-unix:/tmp/.X11-unix python-cipher

# Запуск (Windows с VcXsrv)
docker run -it --rm -e DISPLAY=host.docker.internal:0 python-cipher
```

## Требования

- Python 3.8+
- tkinter (входит в стандартную поставку Python на Windows и macOS)

Для Linux установите:
```bash
sudo apt-get install python3-tk  # Debian/Ubuntu
sudo dnf install python3-tkinter  # Fedora
```

## Структура проекта

```
Python-cipher/
├── *.py                           # CLI-реализации алгоритмов
├── GUI/
│   ├── Visual_Algorithms_final.py # Главное GUI-приложение
│   ├── *.py                       # GUI-адаптеры алгоритмов
├── ec.py                          # Эллиптические кривые (модуль)
├── file.txt                       # Тестовый файл для AES
├── Dockerfile                     # Контейнеризация
├── requirements.txt               # Зависимости
└── README.md
```

## Стек

- Python 3.x
- tkinter + ttk (GUI с тёмной темой)
- Docker (опционально)

## Лицензия

GNU Affero General Public License v3.0 or later.
Полный текст: [LICENSE](LICENSE) и [GNU AGPL v3](https://www.gnu.org/licenses/agpl-3.0.html)

## Примечание

Это учебный проект. Он не проходил независимый аудит и не предназначен для защиты реальных данных.

---

**Автор**: [therudywolf](https://github.com/therudywolf)
