#!/usr/bin/env python3

"""Settings window"""

import tkinter as tk

from core.i18n import I18n

class Settings(tk.Toplevel):
    def __init__(self, lang, master=None):
        super().__init__(master=master)
        self.master = master
        self.lang = lang
        self.i18n = I18n(language=self.lang)
        self.title(self.i18n.t("settings.title"))
        self.geometry("600x600")

        self._gui()

    def _gui(self):
        pass