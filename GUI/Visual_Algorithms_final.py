import os
import sys
import tkinter as tk
from tkinter import messagebox, ttk

_REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if _REPO_ROOT not in sys.path:
    sys.path.insert(0, _REPO_ROOT)

from cipher_suite.asymmetric.elgamal import ElGamal_realisation
from cipher_suite.asymmetric.gost_34_10_94 import GOST_34_10_94_realisation
from cipher_suite.asymmetric.gost_34_10_2012 import GOST_34_10_2012_realisation
from cipher_suite.asymmetric.rsa import RSA_realisation
from cipher_suite.classical.atbash import decrypt as atbash_decrypt, encrypt as atbash_encrypt
from cipher_suite.classical.belazo import decrypt as belazo_decrypt, encrypt as belazo_encrypt
from cipher_suite.classical.caesar import decrypt as cesar_decrypt, encrypt as cesar_encrypt
from cipher_suite.classical.matrix import MatrixLength, alpha, check_errors, encrypt_decrypt
from cipher_suite.classical.playfair import playfer_crypt, playfer_decrypt
from cipher_suite.classical.polibiy import decrypt as polibiy_decrypt, encrypt as polibiy_encrypt
from cipher_suite.classical.tritemius import decrypt as tritemiy_decrypt, encrypt as tritemiy_encrypt
from cipher_suite.classical.vertical import vertical_change
from cipher_suite.classical.vigener import decrypt as vigener_decrypt, encrypt as vigener_encrypt
from cipher_suite.modern.a5_first import a5_realisation
from cipher_suite.modern.a5_second import a52_realisation
from cipher_suite.modern.aes import AES_realize
from cipher_suite.modern.diffie_hellman import compute_shared_secret
from cipher_suite.modern.magma import Gamma, GammaOBR, imitovstavka, prZamena
from cipher_suite.modern.reshetka_kardano import reshetka_kardano
from cipher_suite.modern.vernam import notepad_shenona

ALGORITHMS = [
    "Атбаш", "Цезарь", "Полибий", "Тритемий", "Белазо", "Виженер",
    "Матричный", "Плейфер", "Вертикальная перестановка",
    "Решётка Кардано", "Одноразовый блокнот Шеннона",
    "A5/1", "A5/2", "AES",
    "Магма (Простая замена)", "Магма (Гаммирование)",
    "Магма (Обратное гаммирование)", "Магма (Имитовставка)",
    "RSA", "El Gamal", "ГОСТ 34.10-94", "ГОСТ 34.10-2012"
]

ALGO_MAP = {name: idx + 1 for idx, name in enumerate(ALGORITHMS)}

ALGO_HELP = {
    "Атбаш": {"key_label": "Ключ не требуется", "hint": "Симметричное преобразование без ключа.", "needs_key": False},
    "Цезарь": {"key_label": "Сдвиг", "hint": "Введите целое число для сдвига алфавита.", "needs_key": True},
    "Полибий": {"key_label": "Ключ не требуется", "hint": "Работает с кодированием символов по таблице.", "needs_key": False},
    "Тритемий": {"key_label": "Ключ не требуется", "hint": "Прогрессивный сдвиг без отдельного ключа.", "needs_key": False},
    "Белазо": {"key_label": "Текстовый ключ", "hint": "Введите буквенный ключ той же раскладки.", "needs_key": True},
    "Виженер": {"key_label": "Текстовый ключ", "hint": "Введите короткий буквенный ключ.", "needs_key": True},
    "Матричный": {"key_label": "Ключ 9 символов", "hint": "Ключ должен быть длиной ровно 9 символов.", "needs_key": True},
    "Плейфер": {"key_label": "Текстовый ключ", "hint": "Ключ формирует таблицу Плейфера.", "needs_key": True},
    "Вертикальная перестановка": {"key_label": "Текстовый ключ", "hint": "Ключ задает порядок столбцов.", "needs_key": True},
    "Решётка Кардано": {"key_label": "Размер матрицы", "hint": "Введите целое число для размера квадратной матрицы.", "needs_key": True},
    "Одноразовый блокнот Шеннона": {"key_label": "Ключ не требуется", "hint": "Ключ генерируется автоматически при каждом запуске.", "needs_key": False},
    "A5/1": {"key_label": "Ключ не требуется", "hint": "Потоковый шифр с автоматически сгенерированной гаммой.", "needs_key": False},
    "A5/2": {"key_label": "Ключ не требуется", "hint": "Потоковый шифр с автоматически сгенерированной гаммой.", "needs_key": False},
    "AES": {"key_label": "Ключ AES", "hint": "Используйте английские символы. Практически ожидается ключ до 16 символов.", "needs_key": True},
    "Магма (Простая замена)": {"key_label": "Ключ не требуется", "hint": "Результат выводится в учебном формате.", "needs_key": False},
    "Магма (Гаммирование)": {"key_label": "Ключ не требуется", "hint": "Результат выводится с промежуточными значениями.", "needs_key": False},
    "Магма (Обратное гаммирование)": {"key_label": "Ключ не требуется", "hint": "Результат выводится с промежуточными значениями.", "needs_key": False},
    "Магма (Имитовставка)": {"key_label": "Ключ не требуется", "hint": "Этот режим формирует имитовставку, а не обратимое шифрование.", "needs_key": False},
    "RSA": {"key_label": "Режим подписи", "hint": "Кнопка шифрования создает подпись, кнопка расшифрования выполняет проверку.", "needs_key": False},
    "El Gamal": {"key_label": "Режим подписи", "hint": "Кнопка шифрования создает подпись, кнопка расшифрования выполняет проверку.", "needs_key": False},
    "ГОСТ 34.10-94": {"key_label": "Режим подписи", "hint": "Кнопка шифрования создает подпись, кнопка расшифрования выполняет проверку.", "needs_key": False},
    "ГОСТ 34.10-2012": {"key_label": "Режим подписи", "hint": "Кнопка шифрования создает подпись, кнопка расшифрования выполняет проверку.", "needs_key": False},
}

DARK_BG = "#1e1e2e"
DARK_SURFACE = "#2d2d3f"
DARK_BORDER = "#3d3d5c"
ACCENT = "#7c3aed"
ACCENT_HOVER = "#6d28d9"
TEXT_PRIMARY = "#e2e8f0"
TEXT_SECONDARY = "#94a3b8"
SUCCESS = "#10b981"
ERROR = "#ef4444"


# --- Main GUI Application ---
class CipherApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Python Cipher Suite")
        self.root.geometry("750x650")
        self.root.configure(bg=DARK_BG)
        self.root.minsize(700, 600)

        self.code = ''
        self.selected_algo = tk.StringVar(value=ALGORITHMS[0])
        self.result_var = tk.StringVar(value="")

        self._setup_styles()
        self._build_ui()
        self._on_algo_change()

    def _setup_styles(self):
        style = ttk.Style()
        style.theme_use('clam')

        style.configure('TFrame', background=DARK_BG)
        style.configure('Surface.TFrame', background=DARK_SURFACE)
        style.configure('TLabel', background=DARK_BG, foreground=TEXT_PRIMARY, font=('Segoe UI', 10))
        style.configure('Title.TLabel', background=DARK_BG, foreground=TEXT_PRIMARY, font=('Segoe UI', 18, 'bold'))
        style.configure('Subtitle.TLabel', background=DARK_BG, foreground=TEXT_SECONDARY, font=('Segoe UI', 9))
        style.configure('Section.TLabel', background=DARK_SURFACE, foreground=TEXT_PRIMARY, font=('Segoe UI', 10, 'bold'))

        style.configure('TCombobox', fieldbackground=DARK_SURFACE, background=DARK_SURFACE,
                        foreground=TEXT_PRIMARY, selectbackground=ACCENT, borderwidth=1)
        style.map('TCombobox', fieldbackground=[('readonly', DARK_SURFACE)])

        style.configure('Accent.TButton', background=ACCENT, foreground='white',
                        font=('Segoe UI', 10, 'bold'), padding=(20, 10), borderwidth=0)
        style.map('Accent.TButton', background=[('active', ACCENT_HOVER)])

        style.configure('Secondary.TButton', background=DARK_BORDER, foreground=TEXT_PRIMARY,
                        font=('Segoe UI', 10), padding=(15, 8), borderwidth=0)
        style.map('Secondary.TButton', background=[('active', DARK_SURFACE)])

        style.configure('Success.TButton', background=SUCCESS, foreground='white',
                        font=('Segoe UI', 10, 'bold'), padding=(15, 8), borderwidth=0)

    def _build_ui(self):
        main_frame = ttk.Frame(self.root, style='TFrame', padding=20)
        main_frame.pack(fill=tk.BOTH, expand=True)

        # Header
        header = ttk.Frame(main_frame, style='TFrame')
        header.pack(fill=tk.X, pady=(0, 15))
        ttk.Label(header, text="Python Cipher Suite", style='Title.TLabel').pack(side=tk.LEFT)
        ttk.Label(header, text="v2.0 — Образовательный инструмент криптографии",
                  style='Subtitle.TLabel').pack(side=tk.LEFT, padx=(15, 0), pady=(8, 0))

        # Algorithm selection
        algo_frame = ttk.Frame(main_frame, style='TFrame')
        algo_frame.pack(fill=tk.X, pady=(0, 12))
        ttk.Label(algo_frame, text="Алгоритм:", style='TLabel').pack(side=tk.LEFT, padx=(0, 10))
        self.combo = ttk.Combobox(algo_frame, textvariable=self.selected_algo, values=ALGORITHMS,
                                  state='readonly', width=40, font=('Segoe UI', 10))
        self.combo.pack(side=tk.LEFT, fill=tk.X, expand=True)
        self.combo.bind("<<ComboboxSelected>>", self._on_algo_change)

        self.algo_hint = ttk.Label(main_frame, text="", style='Subtitle.TLabel')
        self.algo_hint.pack(fill=tk.X, pady=(0, 10))

        # Input fields
        input_frame = ttk.Frame(main_frame, style='TFrame')
        input_frame.pack(fill=tk.BOTH, expand=True, pady=(0, 12))

        # Text input
        text_label_frame = ttk.Frame(input_frame, style='TFrame')
        text_label_frame.pack(fill=tk.X, pady=(0, 4))
        ttk.Label(text_label_frame, text="Текст для обработки:", style='TLabel').pack(side=tk.LEFT)

        text_box = ttk.Frame(input_frame, style='Surface.TFrame')
        text_box.pack(fill=tk.X, pady=(0, 10))
        self.text_input = tk.Text(text_box, height=5, bg=DARK_SURFACE, fg=TEXT_PRIMARY,
                                  insertbackground=TEXT_PRIMARY, font=('Consolas', 11),
                                  relief=tk.FLAT, borderwidth=0, padx=10, pady=8,
                                  selectbackground=ACCENT, wrap=tk.WORD)
        text_scroll = tk.Scrollbar(text_box, command=self.text_input.yview)
        self.text_input.configure(yscrollcommand=text_scroll.set)
        self.text_input.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        text_scroll.pack(side=tk.RIGHT, fill=tk.Y)

        # Key input
        key_frame = ttk.Frame(input_frame, style='TFrame')
        key_frame.pack(fill=tk.X, pady=(0, 4))
        self.key_label = ttk.Label(key_frame, text="Ключ", style='TLabel')
        self.key_label.pack(side=tk.LEFT)

        self.key_input = tk.Entry(input_frame, bg=DARK_SURFACE, fg=TEXT_PRIMARY,
                                  insertbackground=TEXT_PRIMARY, font=('Consolas', 11),
                                  relief=tk.FLAT, borderwidth=0)
        self.key_input.pack(fill=tk.X, ipady=8, pady=(0, 15))
        self.key_hint = ttk.Label(input_frame, text="", style='Subtitle.TLabel')
        self.key_hint.pack(fill=tk.X, pady=(0, 12))

        # Buttons
        btn_frame = ttk.Frame(main_frame, style='TFrame')
        btn_frame.pack(fill=tk.X, pady=(0, 15))

        encrypt_btn = tk.Button(btn_frame, text="Зашифровать", bg=ACCENT, fg='white',
                                font=('Segoe UI', 11, 'bold'), relief=tk.FLAT, cursor='hand2',
                                activebackground=ACCENT_HOVER, activeforeground='white',
                                padx=25, pady=10, command=self._encrypt)
        encrypt_btn.pack(side=tk.LEFT, padx=(0, 10))

        decrypt_btn = tk.Button(btn_frame, text="Расшифровать", bg=DARK_BORDER, fg=TEXT_PRIMARY,
                                font=('Segoe UI', 11, 'bold'), relief=tk.FLAT, cursor='hand2',
                                activebackground=DARK_SURFACE, activeforeground=TEXT_PRIMARY,
                                padx=25, pady=10, command=self._decrypt)
        decrypt_btn.pack(side=tk.LEFT, padx=(0, 10))

        clear_btn = tk.Button(btn_frame, text="Очистить", bg=DARK_SURFACE, fg=TEXT_SECONDARY,
                              font=('Segoe UI', 10), relief=tk.FLAT, cursor='hand2',
                              activebackground=DARK_BORDER, activeforeground=TEXT_PRIMARY,
                              padx=15, pady=10, command=self._clear)
        clear_btn.pack(side=tk.LEFT, padx=(0, 10))

        copy_btn = tk.Button(btn_frame, text="Копировать", bg=DARK_SURFACE, fg=TEXT_PRIMARY,
                             font=('Segoe UI', 10), relief=tk.FLAT, cursor='hand2',
                             activebackground=DARK_BORDER, activeforeground=TEXT_PRIMARY,
                             padx=15, pady=10, command=self._copy_result)
        copy_btn.pack(side=tk.LEFT, padx=(0, 10))

        dh_btn = tk.Button(btn_frame, text="Диффи-Хэллман", bg=DARK_SURFACE, fg=SUCCESS,
                           font=('Segoe UI', 10), relief=tk.FLAT, cursor='hand2',
                           activebackground=DARK_BORDER, activeforeground=SUCCESS,
                           padx=15, pady=10, command=self._open_diffie_hellman)
        dh_btn.pack(side=tk.RIGHT)

        # Result
        result_label_frame = ttk.Frame(main_frame, style='TFrame')
        result_label_frame.pack(fill=tk.X, pady=(0, 4))
        ttk.Label(result_label_frame, text="Результат:", style='TLabel').pack(side=tk.LEFT)

        result_box = ttk.Frame(main_frame, style='Surface.TFrame')
        result_box.pack(fill=tk.BOTH, expand=True)
        self.result_output = tk.Text(result_box, height=6, bg=DARK_SURFACE, fg=SUCCESS,
                                     font=('Consolas', 11), relief=tk.FLAT, borderwidth=0,
                                     padx=10, pady=8, wrap=tk.WORD, state=tk.DISABLED,
                                     selectbackground=ACCENT)
        result_scroll = tk.Scrollbar(result_box, command=self.result_output.yview)
        self.result_output.configure(yscrollcommand=result_scroll.set)
        self.result_output.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        result_scroll.pack(side=tk.RIGHT, fill=tk.Y)

    def _get_text(self):
        return self.text_input.get("1.0", tk.END).strip()

    def _get_key(self):
        return self.key_input.get().strip()

    def _on_algo_change(self, _event=None):
        meta = ALGO_HELP.get(self.selected_algo.get(), {})
        self.key_label.config(text=meta.get("key_label", "Ключ"))
        self.key_hint.config(text=meta.get("hint", ""))
        self.algo_hint.config(text=meta.get("hint", ""))
        if meta.get("needs_key", True):
            self.key_input.config(state=tk.NORMAL)
        else:
            self.key_input.delete(0, tk.END)
            self.key_input.config(state=tk.DISABLED)

    def _show_result(self, text, is_error=False):
        self.result_output.config(state=tk.NORMAL)
        self.result_output.delete("1.0", tk.END)
        self.result_output.config(fg=ERROR if is_error else SUCCESS)
        self.result_output.insert("1.0", text)
        self.result_output.config(state=tk.DISABLED)

    def _copy_result(self):
        text = self.result_output.get("1.0", tk.END).strip()
        if not text:
            return
        self.root.clipboard_clear()
        self.root.clipboard_append(text)

    def _encrypt(self):
        algo = self.selected_algo.get()
        text = self._get_text()
        key = self._get_key()

        if not text:
            self._show_result("Введите текст для шифрования!", is_error=True)
            return

        try:
            if algo == "Атбаш":
                result = atbash_encrypt(text)
                self.code = result
                self._show_result(result)

            elif algo == "Цезарь":
                if not key:
                    self._show_result("Введите числовой ключ (дистанцию)!", is_error=True)
                    return
                result = cesar_encrypt(text, key)
                self.code = result
                self._show_result(result)

            elif algo == "Полибий":
                result = polibiy_encrypt(text)
                self.code = result
                self._show_result(result)

            elif algo == "Тритемий":
                result = tritemiy_encrypt(text)
                self.code = result
                self._show_result(result)

            elif algo == "Белазо":
                if not key:
                    self._show_result("Введите ключ!", is_error=True)
                    return
                result = belazo_encrypt(text, key)
                self.code = result
                self._show_result(result)

            elif algo == "Виженер":
                if not key:
                    self._show_result("Введите ключ!", is_error=True)
                    return
                result = vigener_encrypt(text, key)
                self.code = result
                self._show_result(result)

            elif algo == "Матричный":
                if not key or len(key.upper()) != 9:
                    self._show_result("Ключ должен быть длиной 9 символов!", is_error=True)
                    return
                mainKey = key.upper()
                err = check_errors(mainKey)
                if err:
                    self._show_result(err, is_error=True)
                    return
                msg = text.upper()
                for s in msg:
                    if s not in alpha:
                        msg = msg.replace(s, '')
                while len(msg) % MatrixLength != 0:
                    msg += msg[-1]
                result = encrypt_decrypt('1', msg, mainKey)
                self.code = result
                self._show_result(result)

            elif algo == "Плейфер":
                if not key:
                    self._show_result("Введите ключ!", is_error=True)
                    return
                result = playfer_crypt(text, key.lower())
                self.code = result
                self._show_result(result)

            elif algo == "Вертикальная перестановка":
                if not key:
                    self._show_result("Введите ключ!", is_error=True)
                    return
                enc, _ = vertical_change(text, key)
                self.code = enc
                self._show_result(enc)

            elif algo == "Решётка Кардано":
                if not key or not key.isdigit():
                    self._show_result("Введите размер матрицы (число)!", is_error=True)
                    return
                result = reshetka_kardano(int(key), text)
                self.code = result[0]
                self._show_result(result[0])

            elif algo == "Одноразовый блокнот Шеннона":
                result = notepad_shenona(text)
                self._show_result(result[0] + "\n" + result[1] + "\n" + result[2])

            elif algo == "A5/1":
                result = a5_realisation(text)
                self._show_result(result[0] + "\n" + result[1] + "\n" + result[2] + "\n" + result[3])

            elif algo == "A5/2":
                result = a52_realisation(text)
                self._show_result(result[0] + "\n" + result[1] + "\n" + result[2] + "\n" + result[3])

            elif algo == "AES":
                if not key:
                    self._show_result("Введите ключ (англ., до 16 символов)!", is_error=True)
                    return
                try:
                    os.remove("crypted_file.txt")
                except OSError:
                    pass
                with open('file.txt', 'w') as f:
                    f.write(text)
                AES_realize('1', key)
                with open("crypted_file.txt", 'r') as f2:
                    result = f2.read()
                self.code = result
                self._show_result(result)

            elif algo == "Магма (Простая замена)":
                result = prZamena(text)
                self._show_result("16-ричное сообщение:\n" + result[0] + "\nЗашифровано:\n" + result[1])

            elif algo == "Магма (Гаммирование)":
                result = Gamma(text)
                self._show_result("Дополненное сообщение:\n" + result[0] + "\nЗашифровано:\n" + result[1])

            elif algo == "Магма (Обратное гаммирование)":
                result = GammaOBR(text)
                self._show_result("Дополненное сообщение:\n" + result[0] + "\nЗашифровано:\n" + result[1])

            elif algo == "Магма (Имитовставка)":
                result = imitovstavka(text)
                self._show_result("16-ричное сообщение:\n" + result[0] + "\nИмитовставка:\n" + result[1])

            elif algo == "RSA":
                result = RSA_realisation(text)
                self._show_result("ЭЦП:\n" + result[0])
                self._rsa_result = result

            elif algo == "El Gamal":
                result = ElGamal_realisation(text)
                self._show_result("ЭЦП:\n" + result[0])
                self._elgamal_result = result

            elif algo == "ГОСТ 34.10-94":
                result = GOST_34_10_94_realisation(text)
                self._show_result("ЭЦП:\n" + result[0])
                self._gost94_result = result

            elif algo == "ГОСТ 34.10-2012":
                result = GOST_34_10_2012_realisation(text.lower())
                self._show_result("ЭЦП:\n" + result[0])
                self._gost2012_result = result

        except Exception as e:
            self._show_result(f"Ошибка: {str(e)}", is_error=True)

    def _decrypt(self):
        algo = self.selected_algo.get()
        text = self._get_text()
        key = self._get_key()

        if not text and not self.code:
            self._show_result("Введите текст для расшифровки!", is_error=True)
            return

        try:
            if algo == "Атбаш":
                src = self.code if self.code else text
                result = atbash_decrypt(src)
                self._show_result(result)

            elif algo == "Цезарь":
                if not key:
                    self._show_result("Введите числовой ключ!", is_error=True)
                    return
                src = self.code if self.code else text
                result = cesar_decrypt(src, key)
                self._show_result(result)

            elif algo == "Полибий":
                src = self.code if self.code else text
                result = polibiy_decrypt(src)
                self._show_result(result)

            elif algo == "Тритемий":
                src = self.code if self.code else text
                result = tritemiy_decrypt(src)
                self._show_result(result)

            elif algo == "Белазо":
                if not key:
                    self._show_result("Введите ключ!", is_error=True)
                    return
                src = self.code if self.code else text
                result = belazo_decrypt(src, key)
                self._show_result(result)

            elif algo == "Виженер":
                if not key:
                    self._show_result("Введите ключ!", is_error=True)
                    return
                src = self.code if self.code else text
                result = vigener_decrypt(src, key)
                self._show_result(result)

            elif algo == "Матричный":
                if not key or len(key.upper()) != 9:
                    self._show_result("Ключ должен быть длиной 9 символов!", is_error=True)
                    return
                mainKey = key.upper()
                err = check_errors(mainKey)
                if err:
                    self._show_result(err, is_error=True)
                    return
                src = self.code if self.code else text.upper()
                while len(src) % MatrixLength != 0:
                    src += src[-1]
                result = encrypt_decrypt('2', src, mainKey)
                self._show_result(result)

            elif algo == "Плейфер":
                if not key:
                    self._show_result("Введите ключ!", is_error=True)
                    return
                src = self.code if self.code else text
                result = playfer_decrypt(src, key.lower())
                self._show_result(result)

            elif algo == "Вертикальная перестановка":
                if not key:
                    self._show_result("Введите ключ!", is_error=True)
                    return
                _, dec = vertical_change(text, key)
                self._show_result(dec)

            elif algo == "Решётка Кардано":
                if not key or not key.isdigit():
                    self._show_result("Введите размер матрицы (число)!", is_error=True)
                    return
                result = reshetka_kardano(int(key), text)
                self._show_result(result[1])

            elif algo == "Одноразовый блокнот Шеннона":
                result = notepad_shenona(text)
                self._show_result(result[3] + "\n" + result[4])

            elif algo == "A5/1":
                result = a5_realisation(text)
                self._show_result(result[4] + "\n" + result[5])

            elif algo == "A5/2":
                result = a52_realisation(text)
                self._show_result(result[4] + "\n" + result[5])

            elif algo == "AES":
                if not key:
                    self._show_result("Введите ключ!", is_error=True)
                    return
                try:
                    os.remove("decrypted_crypted_file.txt")
                except OSError:
                    pass
                with open("crypted_file.txt", "w") as f:
                    f.write(text if text else self.code)
                AES_realize('2', key)
                with open("decrypted_crypted_file.txt", 'r') as f2:
                    result = f2.read()
                self._show_result(result)

            elif algo == "Магма (Простая замена)":
                result = prZamena(text)
                self._show_result("Расшифровано (16-рич):\n" + result[2] + "\nРасшифрованный текст:\n" + result[3])

            elif algo == "Магма (Гаммирование)":
                result = Gamma(text)
                self._show_result("Расшифрованное сообщение:\n" + result[2])

            elif algo == "Магма (Обратное гаммирование)":
                result = GammaOBR(text)
                self._show_result("Расшифрованное сообщение:\n" + result[2])

            elif algo == "Магма (Имитовставка)":
                self._show_result("Имитовставку нельзя расшифровать!", is_error=True)

            elif algo == "RSA":
                if hasattr(self, '_rsa_result'):
                    self._show_result("Проверка ЭЦП:\n" + self._rsa_result[1])
                else:
                    self._show_result("Сначала создайте ЭЦП (нажмите Зашифровать)!", is_error=True)

            elif algo == "El Gamal":
                if hasattr(self, '_elgamal_result'):
                    self._show_result("Проверка ЭЦП:\n" + self._elgamal_result[1])
                else:
                    self._show_result("Сначала создайте ЭЦП (нажмите Зашифровать)!", is_error=True)

            elif algo == "ГОСТ 34.10-94":
                if hasattr(self, '_gost94_result'):
                    self._show_result("Проверка ЭЦП:\n" + self._gost94_result[1])
                else:
                    self._show_result("Сначала создайте ЭЦП (нажмите Зашифровать)!", is_error=True)

            elif algo == "ГОСТ 34.10-2012":
                if hasattr(self, '_gost2012_result'):
                    self._show_result("Проверка ЭЦП:\n" + self._gost2012_result[1])
                else:
                    self._show_result("Сначала создайте ЭЦП (нажмите Зашифровать)!", is_error=True)

        except Exception as e:
            self._show_result(f"Ошибка: {str(e)}", is_error=True)

    def _clear(self):
        self.text_input.delete("1.0", tk.END)
        self.key_input.delete(0, tk.END)
        self.result_output.config(state=tk.NORMAL)
        self.result_output.delete("1.0", tk.END)
        self.result_output.config(state=tk.DISABLED)
        self.code = ''

    def _open_diffie_hellman(self):
        DiffieHellmanWindow(self.root)


class DiffieHellmanWindow(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Обмен ключами Диффи-Хэллмана")
        self.geometry("450x420")
        self.configure(bg=DARK_BG)
        self.resizable(False, False)
        self._build_ui()

    def _build_ui(self):
        frame = ttk.Frame(self, style='TFrame', padding=25)
        frame.pack(fill=tk.BOTH, expand=True)

        ttk.Label(frame, text="Диффи-Хэллман", style='Title.TLabel').pack(pady=(0, 5))
        ttk.Label(frame, text="Протокол обмена ключами", style='Subtitle.TLabel').pack(pady=(0, 20))

        fields = [
            ("Простое число P:", "p"),
            ("Натуральное число G:", "g"),
            ("Секретное число Алисы:", "ka"),
            ("Секретное число Боба:", "kb"),
        ]

        self.entries = {}
        for label_text, name in fields:
            row = ttk.Frame(frame, style='TFrame')
            row.pack(fill=tk.X, pady=5)
            ttk.Label(row, text=label_text, style='TLabel', width=25).pack(side=tk.LEFT)
            entry = tk.Entry(row, bg=DARK_SURFACE, fg=TEXT_PRIMARY, insertbackground=TEXT_PRIMARY,
                             font=('Consolas', 11), relief=tk.FLAT, width=15)
            entry.pack(side=tk.LEFT, fill=tk.X, expand=True, ipady=5)
            self.entries[name] = entry

        btn = tk.Button(frame, text="Обмен ключами", bg=SUCCESS, fg='white',
                        font=('Segoe UI', 11, 'bold'), relief=tk.FLAT, cursor='hand2',
                        activebackground='#059669', activeforeground='white',
                        padx=20, pady=10, command=self._exchange)
        btn.pack(pady=20)

        self.result_label = tk.Label(frame, text="", bg=DARK_BG, fg=TEXT_PRIMARY,
                                     font=('Consolas', 10), justify=tk.LEFT, wraplength=400)
        self.result_label.pack(fill=tk.X)

    def _exchange(self):
        try:
            p = int(self.entries['p'].get())
            g = int(self.entries['g'].get())
            ka = int(self.entries['ka'].get())
            kb = int(self.entries['kb'].get())

            YA, YB, K1, K2 = compute_shared_secret(p, g, ka, kb)

            result = (
                f"Открытый ключ Алисы: {YA}\n"
                f"Открытый ключ Боба: {YB}\n"
                f"Общий секретный ключ: {K1}"
            )
            if K1 == K2:
                result += "\n\nКлючи совпали!"
            self.result_label.config(text=result, fg=SUCCESS)
        except ValueError as e:
            messagebox.showinfo("Ошибка", str(e) if str(e) else "Введите корректные числа!")
        except Exception as e:
            messagebox.showinfo("Ошибка", str(e))


if __name__ == "__main__":
    root = tk.Tk()
    app = CipherApp(root)
    root.mainloop()
