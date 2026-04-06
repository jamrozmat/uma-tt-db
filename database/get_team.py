#!/usr/bin/env python3

import json

from pathlib import Path

def load_team(app_path):
    json_path = Path(f"{app_path}/tt.json")
    if not json_path.exists() or json_path.stat().st_size == 0:
            return {}
    with open(json_path, "r", encoding="utf-8") as f:
        results = json.load(f)
    return results
