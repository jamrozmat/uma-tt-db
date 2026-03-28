#!/usr/bin/env python3

from setup.config import lang_set
from setup.config import lang_load
from gui.window.lang import ask_lang

def lang_check(app_path):
    if not lang_set(app_path):
        ask_lang(app_path)
    else:
        lang = lang_load(app_path)
        return lang