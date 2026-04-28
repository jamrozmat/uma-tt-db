#!/usr/bin/env python3

import sqlite3

from setup.config import load_db_path

def add_trial_to_db(date: str, hour: str, app_path,
                    points=None, rival_nick=None,
                    class_id=None, diff_id=None):
    try:
        db_path = load_db_path(app_path)
        con = sqlite3.connect(db_path)
        cur = con.cursor()

        rival_id = None
        if rival_nick:
            cur.execute("SELECT Rival_ID FROM Rivals WHERE Rival_Nickname = ?", (rival_nick,))
            result = cur.fetchone()
            if result:
                rival_id = result[0]
            else:
                cur.execute("INSERT INTO Rivals (Rival_Nickname) VALUES (?)", (rival_nick,))
                rival_id = cur.lastrowid

        sql = """
            INSERT INTO Trials (
                Trial_Date, Trial_Time, Points, Rival_ID, Class_ID, Difficulty_ID, is_added
            ) VALUES (?, ?, ?, ?, ?, ?, 0)
            """
        cur.execute(sql, (date, hour, points, rival_id, class_id, diff_id))
        con.commit()
        con.close()
        return True, None
    except sqlite3.Error as e:
        if con: con.rollback()
        return False, e