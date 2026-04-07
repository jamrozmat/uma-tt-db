#!/usr/bin/env python3

import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

from core.i18n import I18n
from core.tooltip import ToolTip
from database.add_uma import add_uma
from database.get_distances import get_distances

class AddUma(tk.Toplevel):
    def __init__(self, lang, app_path, master=None):
        super().__init__(master=master)
        self.master = master
        self.i18n = I18n(language=lang)
        self.app_path = app_path

        title_text = f"{self.i18n.t("uma_add.add_uma")}"
        self.title(title_text)
        self.geometry("250x280")
        self.resizable(width=False, height=False)

        self._gui()

    def _gui(self):
        info_text = f"{self.i18n.t("uma_add.info")}"
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
            text=f"{self.i18n.t("uma_add.name")}: ",
            font=("Helvetica", 10),
        )
        self.name_text_label.grid(row=0, column=0, sticky="w")
        self.name_entry = tk.Entry(self.new_uma_frame, width=20)
        self.name_entry.grid(row=0, column=1)

        self.rank_text_label = tk.Label(
            self.new_uma_frame,
            text=f"{self.i18n.t("uma_add.rank")}: ",
            font=("Helvetica", 10),
        )
        self.rank_text_label.grid(row=1, column=0, sticky="w")
        ToolTip(self.rank_text_label, self.i18n.t("uma_add.rank_info"))
        self.rank_entry = tk.Entry(self.new_uma_frame, width=20)
        self.rank_entry.grid(row=1, column=1)

        self.new_uma_frame.columnconfigure(0, weight=1)
        self.new_uma_frame.columnconfigure(1, weight=2)

        self.distance_frame = tk.Frame(self, padx=10, pady=15)
        self.distance_frame.grid()
        self.distance_text_label = tk.Label(
            self.distance_frame,
            text=f"{self.i18n.t("uma_add.dist")}: ",
            font=("Helvetica", 10),
        )
        self.distance_text_label.grid(row=0, column=0)

        self.distance_data = get_distances(self.app_path)
        distance_name = [row[1] for row in self.distance_data]
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
            text=f"{self.i18n.t("uma_add.exit")}",
            font=("Helvetica", 10),
            relief="solid",
            borderwidth=1,
            command=lambda: self._quit(),
        )
        self.exit.grid(row=0, column=0, padx=5)

        self.add_uma_btn = tk.Button(
            self.btn_frame,
            text=f"{self.i18n.t("uma_add.add_uma")}",
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
        name = self.name_entry.get().strip()
        rank = self.rank_entry.get().strip()
        distance = self.distance.get()
        id_distance = None
        for row in self.distance_data:
            if row[1] == distance:
                id_distance = row[0]
                break

        if name == "" or rank == "" or id_distance is None:
            messagebox.showwarning(f"{self.i18n.t("m_b.error")}!", f"{self.i18n.t("m_b.all_entries")}!")
            return

        try:
            rank = int(rank)
        except ValueError:
            messagebox.showwarning(f"{self.i18n.t("m_b.error")}!", f"{self.i18n.t("m_b.integer")}!")
            return

        success, error = add_uma(name, rank, id_distance, self.app_path)
        if not success:
            messagebox.showerror(f"{self.i18n.t("m_b.db_error")}", f"{self.i18n.t("m_b.cant_save")}:\n{error}")
        else:
            pass

        self.name_entry.delete(0, tk.END)
        self.rank_entry.delete(0, tk.END)
        self.distance.set("")
        self.name_entry.focus_set()