#!/usr/bin/env python3

import sqlite3

from setup.config import load_db_path

def load_distances(app_path):
    """Return Distance ID and Name from database."""
    db_path = load_db_path(app_path)
    con = sqlite3.connect(db_path)
    cur = con.cursor()
    cur.execute("SELECT Distance_ID, Distance_Name from Distances")
    rows = cur.fetchall()
    con.close()
    return rows

def load_trials(app_path):
    """Return reversed list with Team Trial Races ID, Date and Time from database."""
    db_path = load_db_path(app_path)
    con = sqlite3.connect(db_path)
    cur = con.cursor()
    cur.execute("SELECT Trial_ID, Trial_Date, Trial_Time FROM Trials ORDER BY Trial_ID DESC")
    rows = cur.fetchall()
    con.close()
    return rows

def all_trials(app_path):
    """Return number of all TT races in database."""
    db_path = load_db_path(app_path)
    con = sqlite3.connect(db_path)
    cur = con.cursor()
    cur.execute("SELECT Trial_ID FROM Trials")
    rows = cur.fetchall()
    con.close()
    return len(rows)

def all_runs(app_path):
    """Return number of all single runs from database."""
    db_path = load_db_path(app_path)
    con = sqlite3.connect(db_path)
    cur = con.cursor()
    cur.execute("SELECT Result_ID FROM Results")
    runs = cur.fetchall()
    con.close()
    return len(runs)

def percent_of_win(app_path) -> float:
    """Return the win percentage based on all runs in the Results table."""
    db_path = load_db_path(app_path)
    con = sqlite3.connect(db_path)
    cur = con.cursor()
    sql = """
        SELECT 100.0 *
            SUM(CASE WHEN Position = 1
                THEN 1 END) /
            COUNT(*) AS percentage
        FROM Results
        """
    cur.execute(sql)
    percent = cur.fetchone()[0]
    con.close()
    if percent:
        return round(percent, 2)

def percent_of_2nd(app_path) -> float:
    """Return the percentage of 2nd places based on all runs in the Results table."""
    db_path = load_db_path(app_path)
    con = sqlite3.connect(db_path)
    cur = con.cursor()
    sql = """
        SELECT 100.0 *
            SUM(CASE WHEN Position = 2
                THEN 1 END) /
            COUNT(*) AS percentage
        FROM Results
        """
    cur.execute(sql)
    percent = cur.fetchone()[0]
    con.close()
    if percent:
        return round(percent, 2)

def percent_of_3rd(app_path) -> float:
    """Return the percentage of 3rd places based on all runs in the Results table."""
    db_path = load_db_path(app_path)
    con = sqlite3.connect(db_path)
    cur = con.cursor()
    sql = """
        SELECT 100.0 *
            SUM(CASE  WHEN Position = 3
                THEN 1 END) /
            count(*) AS percentage
        FROM Results
        """
    cur.execute(sql)
    percent = cur.fetchone()[0]
    con.close()
    if percent:
        return round(percent, 2)