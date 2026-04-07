#!/usr/bin/env python3

"""Help window"""

import tkinter as tk
from PIL import Image, ImageTk

from core.i18n import I18n
from setup.resources import resource_path

class Help(tk.Toplevel):
    def __init__(self, lang, master=None):
        super().__init__(master=master)
        self.master = master
        self.lang = lang
        self.i18n = I18n(language=self.lang)
        self.title(f"{self.i18n.t("help.title")}")
        self.geometry("600x800")

        self._qui()

    def _qui(self):
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)

        self.page_classes = [StartPage, AddUma]
        self.frames = {}
        self.current_index = 0

        for F in self.page_classes:
            page_name = F.__name__
            frame = F(parent=container, controller=self, i18n=self.i18n)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        nav_bar = tk.Frame(self)
        nav_bar.pack(side="bottom", fill="x", pady=10)

        self.btn_prev = tk.Button(
            nav_bar, 
            text=f"< {self.i18n.t("help.previous")}", 
            command=self.go_prev,
            )
        self.btn_prev.pack(side="left", padx=20)

        self.btn_next = tk.Button(
            nav_bar,
            text=f"{self.i18n.t("help.next")} >",
            command=self.go_next,
            )
        self.btn_next.pack(side="right", padx=20)

        self.show_page()

    def show_page(self):
        page_class = self.page_classes[self.current_index]
        page_name = page_class.__name__
        frame = self.frames[page_name]
        frame.tkraise()

        self.btn_prev.config(state="normal" if self.current_index > 0 else "disabled")
        self.btn_next.config(state="normal" if self.current_index < len(self.page_classes) - 1 else "disabled")

    def go_next(self):
        if self.current_index < len(self.page_classes) - 1:
            self.current_index += 1
            self.show_page()

    def go_prev(self):
        if self.current_index > 0:
            self.current_index -= 1
            self.show_page()

class StartPage(tk.Frame):
    def __init__(self, parent, controller, i18n):
        super().__init__(parent)
        self.controller = controller
        self.i18n = i18n

        label = tk.Label(
            self,
            text=f"{self.i18n.t("help.title").upper()}",
            font=("Arial", 18, "bold"))
        label.pack(pady=50)
        tk.Label(self, text=f"{self.i18n.t("help.welcome")}").pack()
        next = tk.Label(self, text=f"{self.i18n.t("help.welcome2")}")
        next.config(font=("TkDefaultFont", 10, "bold"))
        next.pack(pady=25)

        # ! Refactor as it expands:
        tk.Label(
            self,
            text=f"{self.i18n.t("help.authors")}"
            ).pack(pady=60)

class AddUma(tk.Frame):
    def __init__(self, parent, controller, i18n):
        super().__init__(parent)
        self.controller = controller
        self.i18n = i18n

        tk.Label(self,
                 text=f"{self.i18n.t("help.adding_uma")}",
                 font=("Arial", 12, "bold")
                 ).pack(pady=50)
        tk.Label(self, text=f"{self.i18n.t("help.first")}").pack(pady=30)
        tk.Label(self, text=f"{self.i18n.t("help.first2")}").pack()
        tk.Label(self, text=f"{self.i18n.t("help.first3")}").pack()
        img_file = resource_path(f'uma-tt-db/assets/img/add_uma.png')
        img = Image.open(str(img_file))
        self.add_uma_img = ImageTk.PhotoImage(img)
        add_uma = tk.Label(self, image=self.add_uma_img)
        add_uma.pack(pady=10)
        tk.Label(self, text=f"{self.i18n.t("help.first4")}").pack(pady=7)
        tk.Label(self, 
                 text=f"{self.i18n.t("help.first5")}").pack()


# test
if __name__ == '__main__':
    app = tk.Tk()
    app.withdraw()
    a = Help(master=app)
    app.mainloop()