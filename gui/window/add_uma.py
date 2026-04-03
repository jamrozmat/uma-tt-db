#!/usr/bin/env python3

import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

from core.i18n import I18n
from core.tooltip import ToolTip
from database.add_uma import add_uma
from database.get_distances import get_distances

class AddUma(tk.Toplevel):
    def __init__(self, lang, master=None):
        super().__init__(master=master)
        self.master = master
        self.i18n = I18n

        self.title(f"{self.i18n.t("add_uma.add_uma")}")
        self.geometry("250x260")
        self.resizable(width=False, height=False)

        self._gui()

    def _gui(self):
        info_text = f"{self.i18n.t("add_uma.info")}"
        self.info_label = tk.Label(
            self,
            text=info_text,
            font=("Helvetica", 10, "italic"),
            anchor="n",
        )
        self.info_label.config(padx=10, pady=10)
        self.info_label.grid(sticky="n")

        self.new_uma_frame = tk.Frame(self, padx=10, pady=5)
        self.new_uma_frame.grid()

        self.name_text_label = tk.Label(
            self.new_uma_frame,
            text=f"{self.i18n.t("add_uma.name")}: ",
            font=("Helvetica", 10),
        )
        self.name_text_label.grid(row=0, column=0, sticky="w")
        self.name_entry = tk.Entry(self.new_uma_frame, width=20)
        self.name_entry.grid(row=0, column=1)

        self.rank_text_label = tk.Label(
            self.new_uma_frame,
            text=f"{self.i18n.t("add_uma.rank")}: ",
            font=("Helvetica", 10),
        )
        self.rank_text_label.grid(row=1, column=0, sticky="w")
        ToolTip(self.rank_text_label, self.i18n.t("add_uma.rank_info"))
        self.rank_entry = tk.Entry(self.new_uma_frame, width=20)
        self.rank_entry.grid(row=1, column=1)

        self.new_uma_frame.columnconfigure(0, weight=1)
        self.new_uma_frame.columnconfigure(1, weight=2)

        self.distance_frame = tk.Frame(self, padx=10, pady=15)
        self.distance_frame.grid()
        self.distance_text_label = tk.Label(
            self.distance_frame,
            text=f"{self.i18n.t("add_uma.dist")}: ",
            font=("Helvetica", 10),
        )
        self.distance_text_label.grid(row=0, column=0)

        self.distance_data = get_distances()
        distance_name = [row[0] for row in self.distance_data]
        self.distance = ttk.Combobox(
            self.distance_frame,
            values=distance_name,
            state="readonly",
            width=15,
        )
        self.distance.grid(row=1, column=0)

        self.btn_frame = tk.Frame(self)
        self.btn_frame.grid(padx=10, pady=20)

        self.exit = tk.Button(
            self.btn_frame,
            text=f"{self.i18n.t("add_uma.exit")}",
            font=("Helvetica", 10),
            relief="solid",
            borderwidth=1,
            command=lambda: self._quit(),
        )
        self.exit.grid(row=0, column=0, padx=5)

        self.add_uma_btn = tk.Button(
            self.btn_frame,
            text=f"{self.i18n.t("add_uma.add_uma")}",
            font=("Helvetica", 10),
            relief="solid",
            borderwidth=2,
            command=self._add_uma,
        )
        self.add_uma_btn.grid(row=0, column=1, padx=5)

        self.btn_frame.columnconfigure(0, weight=1)
        self.btn_frame.columnconfigure(1, weight=1)

    def _quit(self):
        self.destroy()

    def _add_uma(self):
        name = self.name_entry.get()
        rank = self.rank_entry.get()
        distance = self.distance.get()
        id_distance = None
        for row in self.distance_data:
            if row[1] == distance:
                id_distance = row[0]
                break

        if name == "" or rank == "" or id_distance is None:
            messagebox.showwarning("Error!", "Wypełnij wszystkie pola!")
            return

        try:
            rank = int(rank)
        except ValueError:
            messagebox.showwarning("Error!", "Ocena musi być liczbą!")
            return

        success, error = add_uma(name, rank, id_distance)
        if not success:
            messagebox.showerror("Błąd bazy danych", f"Nie udało się zapisać:\n{error}")
        else:
            pass

        self.name_entry.delete(0, tk.END)
        self.rank_entry.delete(0, tk.END)
        self.distance.set("")
        self.name_entry.focus_set()