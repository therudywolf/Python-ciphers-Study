# 🐺 RudyWolf Cipher Suite

This project is licensed under the GNU Affero General Public License v3.0 or later.
AGPL v3 Copyleft applies to reuse, modification, and network deployment of derived versions.

> Учебный набор классических и современных криптографических алгоритмов с CLI-скриптами и единым Tkinter GUI.

## Что это за проект

- Учебная реализация шифров, перестановок, ЭЦП и обмена ключами.
- Архивный учебный репозиторий RudyWolf с единым FOSS-оформлением.
- Подходит для демонстрации алгоритмов, лабораторных и самостоятельного изучения.
- Не предназначен для production-задач и защиты реальных данных.

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

## Работа с GUI

1. Запустите `python GUI/Visual_Algorithms_final.py`.
2. Выберите алгоритм в выпадающем списке.
3. Введите исходный текст.
4. Если алгоритм требует ключ, GUI покажет тип ключа и краткую подсказку.
5. Нажмите `Зашифровать` или `Расшифровать`. Для RSA, ElGamal и ГОСТ это режимы создания и проверки подписи.

## Требования к ключу

| Алгоритм | Формат ключа |
|----------|--------------|
| Атбаш | не требуется |
| Цезарь | целое число |
| Белазо | текстовый ключ |
| Виженер | текстовый ключ |
| Матричный | ровно 9 символов |
| Плейфер | текстовый ключ |
| Вертикальная перестановка | текстовый ключ |
| Решётка Кардано | целое число |
| AES-128 | строка до 16 символов |

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

## Проверка проекта

```bash
PYTHONDONTWRITEBYTECODE=1 python3 -m compileall -q .
```

Если в рабочей директории есть служебные локальные копии инструментов, например `.claude/`, исключайте их из проверки или держите вне репозитория.

## Структура проекта

```
Python-cipher/
├── *.py                           # CLI-реализации алгоритмов
├── GUI/
│   ├── Visual_Algorithms_final.py # Главное GUI-приложение
│   ├── *.py                       # GUI-адаптеры алгоритмов
├── ec.py                          # Эллиптические кривые (модуль)
├── Dockerfile                     # Контейнеризация
├── requirements.txt               # Зависимости
├── CONTRIBUTING.md                # Правила для изменений
└── README.md
```

## Стек

- Python 3.x
- tkinter + ttk (GUI с тёмной темой)
- Docker (опционально)

## Лицензия

GNU Affero General Public License v3.0 or later.
Полный текст: [LICENSE](LICENSE) и [GNU AGPL v3](https://www.gnu.org/licenses/agpl-3.0.html)

Если вы публикуете измененную сетевую версию этого проекта, AGPL требует предоставить соответствующий исходный код пользователям такого сервиса.

## Вклад

Вклады приветствуются. Правила для изменений описаны в [CONTRIBUTING.md](CONTRIBUTING.md).

## Примечание

Это учебный проект. Он не проходил независимый аудит и не предназначен для защиты реальных данных.
Временные файлы для AES и промежуточные результаты генерируются локально во время запуска и не входят в репозиторий.

---

**Автор**: [therudywolf](https://github.com/therudywolf)
