#!/usr/bin/env python3

import sys
from pathlib import Path

def resource_path(relative: str):
    if hasattr(sys, '_MEIPASS'):
        return Path(sys._MEIPASS) / relative
    else:
        base = Path(__file__).resolve().parents[2]

    return base / relative