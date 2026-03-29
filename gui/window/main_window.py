#!/usr/bin/env python3

import tkinter as tk

from core.i18n import I18n
from core.tooltip import ToolTip
from database.db_manager import pragma

class MainWindow(tk.Toplevel):
    def __init__(self, app_path, lang, __app_name__, master=None):
        super().__init__(master)
        self.master = master
        self.title(__app_name__)
        self.geometry('600x630')

        self.app_path = app_path
        self.lang = lang
        print(">>> WYŚWIETLONO MENU GŁÓWNE <<<")
        self.i18n = I18n(language=lang)

        #self.icon = tk.PhotoImage(file=f'{BASE}/assets/icons/carats.png')
        #self.iconphoto(True, self.icon)
        self._qui()

    def _qui(self):
        # LOGO
        # Due to the lack of suitable CC0-licensed graphics, 
        # I cannot place anything in this section. 
        # If you would like to help by creating your own image, 
        # please contact the program's author.
        logo = tk.Label(
            self, 
            text="Want to help and see your artwork here?\nContact the developer!",
            fg="gray")
        logo.pack(side="top", anchor="n", pady=10)

        version = pragma(self.app_path)
        pragma_text = f"{self.i18n.t("main_menu.pragma")} {version}"
        pragma_label = tk.Label(self, text=pragma_text, fg="gray")
        ToolTip(pragma_label, f"{self.i18n.t("main_menu.pragma_info")}")
        pragma_label.pack(side="top", anchor="nw", padx=10, pady=40)