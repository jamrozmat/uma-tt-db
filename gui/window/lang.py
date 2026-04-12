#!/usr/bin/env python3

import tkinter as tk
from tkinter import ttk

from setup.config import lang_update

def ask_lang(app_path):
    root = tk.Tk()
    root.title("Setting Language")
    root.geometry("200x150")

    window = tk.Frame(root)
    window.pack()

    lang_code = None

    ask = tk.Label(window, text="Choose your language:\nWybierz język:")
    ask.pack(pady=10)

    LANG_MAPPING = {
        "English": "en",
        "Polski": "pl",
        }
    choose = ttk.Combobox(
        window,
        values=list(LANG_MAPPING.keys()),
        state="readonly",
        width=10,
    )
    choose.current(0)
    choose.pack(pady=4)

    def _save():
        nonlocal lang_code
        chosen_lang = choose.get()
        lang_code = LANG_MAPPING.get(chosen_lang)
        lang_update(app_path, lang_code)
        root.destroy()

    btn = tk.Button(window, text="OK", command=_save)
    btn.pack(pady=2)

    root.mainloop()

    return lang_code