#!/usr/bin/env python3

import sqlite3

from setup.config import load_db_path

def get_distances(app_path):
    """
    Return the list with Distance_ID and Distance_Name 
    from the Distances table in the database.
    """
    db_path = load_db_path(app_path)
    con = sqlite3.connect(db_path)
    cur = con.cursor()
    cur.execute("""
                SELECT Distance_ID, Distance_Name
                FROM Distances
                """)
    distances = cur.fetchall()
    con.close()

    return distances