#!/usr/bin/env python3

import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

from database.get_uma import (
    load_umas, load_umas_by_id
)
from database.get_team import load_team
from database.get_distances import get_distances
from database.get_trials import load_trials_short
from database.add_results import add_results_to_db

from core.i18n import I18n
from core.tooltip import ToolTip

class AddResults(tk.Toplevel):
    def __init__(self, app_path, lang, master=None):
        super().__init__(master=master)
        self.master = master
        self.i18n = I18n(language=lang)
        self.title(f"{self.i18n.t("add_results.title")}")
        self.geometry("400x720")

        self.umas = load_umas(app_path)
        self.team = load_team(app_path)
        self.trials = load_trials_short(app_path)
        self.combo_trials = self.trials[::-1]

        self.distances = get_distances(app_path)
        self.roles = ['fr', 'pc', 'ls', 'ec']

        self._gui(app_path)

    def _gui(self, app_path):
        info_text = f"{self.i18n.t("add_results.info")}"
        self.info_label = tk.Label(
            self,
            text=info_text,
            font=("Helvetica", 10, "italic"),
            anchor="n",
        )
        self.info_label.config(padx=10, pady=10)
        self.info_label.pack()

        self.info_row_label = tk.Label(
            self,
            anchor="n",
        )
        self.info_row_label.pack()

        self.help_label = tk.Label(
            self.info_row_label,
            text=" ❓ ",
            fg="red",
            bg="white",
            relief="groove",
            borderwidth=2,
        )
        ToolTip(self.help_label, f"{self.i18n.t("add_results.help")}")
        self.help_label.pack(side="left", expand=True)

        self.trial_combo = ttk.Combobox(
            self.info_row_label,
            values=self.combo_trials,
            state="readonly",
        )
        self.trial_combo.pack(side="left", expand=True, padx=20)

        self.inputs = {}
        uma_ids = [uid for uid in self.team.values() if uid is not None]
        self.umas_dict = load_umas_by_id(uma_ids, app_path)

        dist_names = {row[0]: row[1] for row in self.distances}
        self.dist_frames = {}

        for position, uma_id in self.team.items():
            if uma_id is None:
                continue

            uma_data = self.umas_dict.get(uma_id, {})
            dist_id = uma_data.get("distance")
            dist_name = dist_names.get(dist_id, "Unknown distance")

            if dist_id not in self.dist_frames:
                self.dist_frame = tk.LabelFrame(self,
                                                text=dist_name.upper(),
                                                font=("Helvetica", 12, "bold"),
                                                )
                self.dist_frame.pack(fill="x", padx=10, pady=5)
                self.dist_frames[dist_id] = self.dist_frame

            target_frame = self.dist_frames[dist_id]

            if position not in self.inputs:
                self.inputs[position] = {}

            self.row_frame = tk.Frame(target_frame)
            self.row_frame.pack(fill="x", pady=2)

            name = uma_data.get("name", str(uma_id))
            rating = uma_data.get("rating", "?")

            self.uma_name_label = tk.Label(
                self.row_frame,
                text=f"{name}   ({rating})",
                width=25,
                anchor="w",
            )
            self.uma_name_label.pack(side="left")

            self.input = tk.Entry(self.row_frame, width=20)
            self.input.pack(side="left", padx=20)

            self.inputs[position][uma_id] = self.input

        self.button_row_label = tk.Label(self)
        self.button_row_label.pack(padx=2, pady=20)

        self.back_to_menu = tk.Button(
            self.button_row_label,
            text=f"{self.i18n.t("add_results.exit")}",
            font=("Helvetica", 10),
            relief="solid",
            borderwidth=1,
            command=self._exit,
        )
        self.back_to_menu.pack(side="left", expand=True, padx=20)

        self.save = tk.Button(
            self.button_row_label,
            text=f"{self.i18n.t("add_results.save")}",
            font=("Helvetica", 10, "bold"),
            borderwidth=2,
            command=lambda: self._save(app_path),
        )
        self.save.pack(side="left", expand=True, padx=20)
        self.bind("<Return>", self._save)

    def _save(self, app_path, event=None):
        selected_trial = self.trial_combo.get()
        if not selected_trial:
            messagebox.showerror(f"{self.i18n.t("m_b.no_trial")}", f"{self.i18n.t("m_b.select_trial")}!")
            return
        id_trial = selected_trial.split()[0]

        inputs_to_db = []
        for pos, uma_inputs in self.inputs.items():
            for uma_id, input in uma_inputs.items():
                result = input.get().strip()

                if result:
                    uma_info = self.umas_dict.get(uma_id, {})
                    id_distance = uma_info.get("distance")
                    inputs_to_db.append((id_trial, uma_id, result, id_distance))
        
        if inputs_to_db:
            add_results_to_db(inputs_to_db, app_path)
            self._clear_inputs()
        else:
            messagebox.showerror(f"{self.i18n.t("m_b.no_data")}", f"{self.i18n.t("m_b.all_entries")}")

    def _clear_inputs(self):
        self.trial_combo.set("")
        for pos, uma_inputs in self.inputs.items():
            for uma_id, input in uma_inputs.items():
                input.delete(0, 'end')
        self.trial_combo.focus_set()

    def _exit(self):
        self.destroy()