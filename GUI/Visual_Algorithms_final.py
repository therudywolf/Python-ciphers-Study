"""
Python Ciphers Study - GUI Application
A visual interface for cryptographic algorithms
Licensed under AGPL-3.0
"""

import tkinter as tk
from tkinter import messagebox, ttk
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

try:
    from reshetka_kardano_final import reshetka_kardano
    from vernam import notepad_shenona
    from A5_first import a5_realisation
    from A5_second import a52_realisation
    from AES import AES_realize
    from Magma import prZamena, Gamma, GammaOBR, imitovstavka
    from RSA import RSA_realisation
    from ElGamal import ElGamal_realisation
    from GOST_34_10_94 import GOST_34_10_94_realisation
    from GOST_34_10_2012 import GOST_34_10_2012_realisation
except ImportError as e:
    print(f"Warning: Could not import all modules: {e}")


class CipherGUI:
    """Main GUI Application for Cryptographic Algorithms"""

    def __init__(self, root):
        self.root = root
        self.root.title("🔐 Python Ciphers Study")
        self.root.geometry("900x700")
        self.root.resizable(True, True)
        self.setup_styles()
        self.create_widgets()
        self.encrypted_text = ""
        self.cipher_key = ""

    def setup_styles(self):
        """Configure application styles"""
        style = ttk.Style()
        style.theme_use('clam')
        style.configure('Title.TLabel', font=('Helvetica', 16, 'bold'))
        style.configure('Header.TLabel', font=('Helvetica', 12, 'bold'))
        style.configure('Accent.TButton', font=('Helvetica', 10, 'bold'))

    def create_widgets(self):
        """Create all GUI widgets"""
        main_frame = ttk.Frame(self.root, padding="10")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        title = ttk.Label(main_frame, text="🔐 Cryptographic Cipher Suite", style='Title.TLabel')
        title.grid(row=0, column=0, columnspan=2, pady=10)

        ttk.Label(main_frame, text="Select Algorithm:", style='Header.TLabel').grid(row=1, column=0, sticky=tk.W)

        self.algorithms = [
            "Atbash", "Caesar", "Polybius", "Trithemius", "Belaso",
            "Vigenere", "Matrix", "Playfair", "Vertical Transposition",
            "Cardano Grid", "Vernam (One-Time Pad)",
            "A5/1", "A5/2", "AES",
            "Magma (Substitution)", "Magma (Gamma)", "Magma (Reverse Gamma)", "Magma (Imitation)",
            "RSA", "ElGamal", "GOST 34.10-94", "GOST 34.10-2012"
        ]

        self.cipher_combo = ttk.Combobox(main_frame, values=self.algorithms, state='readonly', width=30)
        self.cipher_combo.grid(row=1, column=1, padx=5)
        self.cipher_combo.current(0)

        ttk.Label(main_frame, text="Input Text:", style='Header.TLabel').grid(row=2, column=0, sticky=tk.W, pady=5)

        self.input_text = tk.Text(main_frame, height=4, width=60, wrap=tk.WORD)
        self.input_text.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

        ttk.Label(main_frame, text="Key/Parameter (if needed):", style='Header.TLabel').grid(row=4, column=0, sticky=tk.W, pady=5)

        self.key_entry = ttk.Entry(main_frame, width=60)
        self.key_entry.grid(row=5, column=0, columnspan=2, padx=5)

        button_frame = ttk.Frame(main_frame)
        button_frame.grid(row=6, column=0, columnspan=2, pady=10)

        ttk.Button(button_frame, text="🔒 Encrypt", command=self.encrypt, style='Accent.TButton').pack(side=tk.LEFT, padx=5)
        ttk.Button(button_frame, text="🔓 Decrypt", command=self.decrypt, style='Accent.TButton').pack(side=tk.LEFT, padx=5)
        ttk.Button(button_frame, text="Clear", command=self.clear_all).pack(side=tk.LEFT, padx=5)

        ttk.Label(main_frame, text="Output:", style='Header.TLabel').grid(row=7, column=0, sticky=tk.W, pady=5)

        self.output_text = tk.Text(main_frame, height=4, width=60, wrap=tk.WORD, state=tk.DISABLED)
        self.output_text.grid(row=8, column=0, columnspan=2, padx=5, pady=5)

        info_frame = ttk.LabelFrame(main_frame, text="ℹ️ Information", padding="5")
        info_frame.grid(row=9, column=0, columnspan=2, sticky=(tk.W, tk.E), padx=5, pady=5)

        self.info_label = ttk.Label(info_frame, text="Select an algorithm to see information", wraplength=500, justify=tk.LEFT)
        self.info_label.pack(fill=tk.BOTH, expand=True)

        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)

    def get_input(self):
        """Get input text from widget"""
        return self.input_text.get("1.0", tk.END).strip()

    def get_key(self):
        """Get key from entry"""
        return self.key_entry.get().strip()

    def display_output(self, text):
        """Display output text"""
        self.output_text.config(state=tk.NORMAL)
        self.output_text.delete("1.0", tk.END)
        self.output_text.insert("1.0", str(text))
        self.output_text.config(state=tk.DISABLED)

    def encrypt(self):
        """Encrypt using selected algorithm"""
        try:
            text = self.get_input()
            if not text:
                messagebox.showwarning("Input Required", "Please enter text to encrypt")
                return

            algorithm = self.cipher_combo.get()
            self.encrypted_text = self.process_cipher(algorithm, text, "encrypt")
            self.display_output(self.encrypted_text)
            messagebox.showinfo("Success", "Text encrypted successfully!")
        except Exception as e:
            messagebox.showerror("Error", f"Encryption failed: {str(e)}")

    def decrypt(self):
        """Decrypt using selected algorithm"""
        try:
            algorithm = self.cipher_combo.get()
            text_to_decrypt = self.encrypted_text if self.encrypted_text else self.get_input()

            if not text_to_decrypt:
                messagebox.showwarning("Input Required", "Please enter text to decrypt")
                return

            result = self.process_cipher(algorithm, text_to_decrypt, "decrypt")
            self.display_output(result)
            messagebox.showinfo("Success", "Text decrypted successfully!")
        except Exception as e:
            messagebox.showerror("Error", f"Decryption failed: {str(e)}")

    def process_cipher(self, algorithm, text, operation):
        """Process cipher operation"""
        key = self.get_key()

        if algorithm == "Caesar":
            if not key or not key.isdigit():
                messagebox.showwarning("Key Required", "Caesar cipher requires numeric key")
                return ""
            return self.caesar_cipher(text, int(key), operation)
        elif algorithm == "Vigenere":
            if not key:
                messagebox.showwarning("Key Required", "Vigenere cipher requires text key")
                return ""
            return self.vigenere_cipher(text, key, operation)
        elif algorithm == "RSA":
            return RSA_realisation(text)
        elif algorithm == "AES":
            return AES_realize(text, key if key else "defaultkey")
        elif algorithm == "ElGamal":
            return ElGamal_realisation(text)
        else:
            messagebox.showinfo("Info", f"{algorithm} cipher - implementation in progress")
            return text

    def caesar_cipher(self, text, shift, operation):
        """Caesar cipher implementation"""
        alphabet_lower = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'
        alphabet_upper = alphabet_lower.upper()
        result = ""

        if operation == "decrypt":
            shift = -shift

        for char in text:
            if char.islower():
                idx = alphabet_lower.find(char)
                if idx != -1:
                    result += alphabet_lower[(idx + shift) % len(alphabet_lower)]
                else:
                    result += char
            elif char.isupper():
                idx = alphabet_upper.find(char)
                if idx != -1:
                    result += alphabet_upper[(idx + shift) % len(alphabet_upper)]
                else:
                    result += char
            else:
                result += char

        return result

    def vigenere_cipher(self, text, key, operation):
        """Vigenere cipher implementation"""
        alphabet = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'
        result = ""
        key_index = 0

        for char in text:
            if char.lower() in alphabet:
                shift = alphabet.find(key[key_index % len(key)].lower())
                if operation == "decrypt":
                    shift = -shift

                char_idx = alphabet.find(char.lower())
                new_idx = (char_idx + shift) % len(alphabet)
                result += alphabet[new_idx].upper() if char.isupper() else alphabet[new_idx]
                key_index += 1
            else:
                result += char

        return result

    def clear_all(self):
        """Clear all text fields"""
        self.input_text.delete("1.0", tk.END)
        self.key_entry.delete(0, tk.END)
        self.output_text.config(state=tk.NORMAL)
        self.output_text.delete("1.0", tk.END)
        self.output_text.config(state=tk.DISABLED)
        self.encrypted_text = ""


def main():
    """Launch the application"""
    root = tk.Tk()
    app = CipherGUI(root)
    root.mainloop()


if __name__ == "__main__":
    main()
