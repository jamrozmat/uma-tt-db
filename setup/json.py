#!/usr/bin/env python3

from pathlib import Path

from setup.config import json_update

def create_json(app_path):
    json_path = Path(f"{app_path}/tt.json")
    json_path.touch(exist_ok=True)
    json_update(app_path, json_path)