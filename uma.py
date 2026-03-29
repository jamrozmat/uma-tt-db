#!/usr/bin/env python3

__author__ = "Mateusz Jamróz"
__version__ = "0.1.0"
__app_name__ = "UmaTT_DB"

import tkinter as tk

from gui.window.main_window import MainWindow
from setup.os_check import check_os
from setup.folders_mng import create_folders
from setup.config import create_config
from setup.json import create_json
from setup.lang import lang_check
from database.db_manager import create_db

def start():
    system = check_os()
    app_path = create_folders(system, __app_name__)
    create_config(app_path)
    create_db(app_path)
    create_json(app_path)
    lang = lang_check(app_path)
    root = tk.Tk()
    root.withdraw()
    MainWindow(app_path, lang, __app_name__, master=root)
    root.mainloop()

if __name__ == '__main__':
    start()