#!/usr/bin/env python3

import sqlite3

from setup.config import load_db_path

def load_umas(app_path):
    db_path = load_db_path(app_path)
    con = sqlite3.connect(db_path)
    cur = con.cursor()
    cur.execute("SELECT Uma_ID, Uma_Name, Uma_Rank FROM Uma")
    rows = cur.fetchall()
    con.close()
    return rows

def load_umas_by_id(uma_ids, app_path):
    db_path = load_db_path(app_path)
    con = sqlite3.connect(db_path)
    cur = con.cursor()
    if not uma_ids:
        return {}
    placeholders = ",".join("?" for _ in uma_ids)
    sql = f"""
    SELECT Uma_ID, Uma_Name, Uma_Rank, Distance_ID
    FROM Uma
    WHERE Uma_ID IN ({placeholders})
    """
    cur.execute(sql, uma_ids)
    return {
        row[0]: {
            "name": row[1],
            "rating": row[2],
            "distance": row[3],
        }
        for row in cur.fetchall()
    }

def load_uma_position(uma_id, app_path):
    db_path = load_db_path(app_path)
    con = sqlite3.connect(db_path)
    cur = con.cursor()

    sql = """
    SELECT t.Trial_Date, t.Trial_Time, r.Position
    FROM Results r
    JOIN Trials t ON r.Trial_ID = t.Trial_ID
    WHERE r.Uma_ID = ?
    ORDER BY t.Trial_Date ASC, t.Trial_Time ASC
    """
    cur.execute(sql, (uma_id,))
    rows = cur.fetchall()
    con.close()
    labels = [f"{row[0]} {row[1]}" for row in rows]
    positions = [row[2] for row in rows]

    return labels, positions

def load_uma_name(uma_id, app_path):
    db_path = load_db_path(app_path)
    con = sqlite3.connect(db_path)
    cur = con.cursor()
    cur.execute(f"SELECT Uma_Name FROM Uma WHERE Uma_ID = {uma_id}")
    name = cur.fetchall()
    con.close()
    if isinstance(name, (list, tuple)):
        name = name[0][0]
        return name
    else:
        return name

def load_umas_by_distance(distance_id, app_path):
    db_path = load_db_path(app_path)
    con = sqlite3.connect(db_path)
    cur = con.cursor()
    sql = "SELECT Uma_ID FROM Uma WHERE Distance_ID = ?"
    cur.execute(sql, (distance_id,))
    umas = cur.fetchall()
    con.close()
    return umas

def load_umas_by_trial(serie_id, app_path):
    db_path = load_db_path(app_path)
    con = sqlite3.connect(db_path)
    cur = con.cursor()
    sql = """
    SELECT Uma.Uma_ID FROM Uma
    JOIN Results on Uma.Uma_ID = Results.Uma_ID
    WHERE Results.Trial_ID = ?
    """
    cur.execute(sql, (serie_id,))
    umas = cur.fetchall()
    con.close()
    return umas