#!/usr/bin/env python3

import tkinter as tk
from tkinter import ttk

from setup.config import lang_update

def ask_lang(app_path):
    root = tk.Tk()
    root.title("Setting Language")
    root.geometry("200x150")

    window = tk.Frame(root)
    window.grid()

    ask = tk.Label(window, text="Choose your language:\nWybierz język:")
    ask.grid(pady=20)

    lang = {
        "English": "eng",
        "Polski": "pl",
        }
    choose = ttk.Combobox(
        window,
        values=list(lang.keys()),
        state="readonly",
        width=10,
    )
    choose.current()
    choose.grid(padx=20, pady=4)

    def _save():
        chosen_lang = choose.get()
        lang_code = lang.get(chosen_lang)
        lang_update(app_path, lang_code)
        root.destroy()

    btn = tk.Button(window, text="OK", command=_save)
    btn.grid(pady=2)

    root.mainloop()