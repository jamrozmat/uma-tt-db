#!/usr/bin/env python3

import sqlite3

from setup.config import load_db_path

def load_type_of_run(app_path):
    db_path = load_db_path(app_path)
    con = sqlite3.connect(db_path)
    cur = con.cursor()
    cur.execute("SELECT Distance_ID, Distance_Name from Distances")
    rows = cur.fetchall()
    con.close()
    formatted = []
    for row in rows:
        line = f"{row[0]}  | {row[1]}"
        formatted.append(line)
    return formatted

def load_trials(app_path):
    db_path = load_db_path(app_path)
    con = sqlite3.connect(db_path)
    cur = con.cursor()
    cur.execute("SELECT Trial_ID, Trial_Date, Trial_Time FROM Trials")
    rows = cur.fetchall()
    con.close()

    formatted = []
    for row in rows:
        line = f"{row[0]}   | {row[1]} | {row[2]}"
        formatted.append(line)
    return formatted[::-1]

def load_trials_short(app_path):
    db_path = load_db_path(app_path)
    con = sqlite3.connect(db_path)
    cur = con.cursor()
    cur.execute("SELECT Trial_ID, Trial_Date, Trial_Time from Trials")
    rows = cur.fetchall()
    con.close()

    formatted = []
    for row in rows:
        line = f"{row[0]}   |  {row[1]}  |  {row[2]}"
        formatted.append(line)

    return formatted[::-1]