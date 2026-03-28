#!/usr/bin/env python3

import tkinter as tk

class MainWindow(tk.Toplevel):
    def __init__(self, app_path, lang, __app_name__, master=None):
        super().__init__(master)
        self.master = master
        self.title(__app_name__)
        self.geometry('600x630')

        self.app_path = app_path
        self.lang = lang
        print(">>> WYŚWIETLONO MENU GŁÓWNE <<<")
        #self.i18n = I18n(language=lang)

        #self.icon = tk.PhotoImage(file=f'{BASE}/assets/icons/carats.png')
        #self.iconphoto(True, self.icon)