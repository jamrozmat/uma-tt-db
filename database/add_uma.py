#!/usr/bin/env python3

import sqlite3

from setup.config import load_db_path

def add_uma(name: str, rank: int, id_distance: int, app_path):
    """Add a new Uma to the database and return an error if the operation fails."""
    db_path = load_db_path(app_path)
    try:
        con = sqlite3.connect(db_path)
        cur = con.cursor()
        sql = """
        INSERT INTO Uma
        (Uma_Name, Uma_Rank, Distance_ID)
        VALUES (?, ?, ?)
        """
        cur.execute(sql, (name, rank, id_distance,))
        con.commit()
        con.close()
        return True, None
    except sqlite3.Error as e:
        return False, e