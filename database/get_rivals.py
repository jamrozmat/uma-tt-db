#!/usr/bin/env python3

import sqlite3

from setup.config import load_db_path

def search_rivals(app_path, text) -> str | None:
    """Search for the first rival nickname starting with the given text."""
    db_path = load_db_path(app_path)
    con = sqlite3.connect(db_path)
    cur = con.cursor()
    cur.execute("SELECT Rival_Nickname FROM Rivals WHERE Rival_Nickname LIKE ? LIMIT 1", (text + '%',))
    rival = cur.fetchone()
    con.close()
    return rival[0] if rival else None