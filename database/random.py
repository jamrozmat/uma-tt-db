#!/usr/bin/env python3

import sqlite3

from setup.config import load_db_path

def all_days_db(app_path):
    """Returns the total count of unique days registered in the Trials table."""
    db_path = load_db_path(app_path)
    con = sqlite3.connect(db_path)
    cur = con.cursor()
    cur.execute("SELECT COUNT(DISTINCT Trial_Date) FROM Trials")
    days = cur.fetchone()[0]
    con.close()
    return days