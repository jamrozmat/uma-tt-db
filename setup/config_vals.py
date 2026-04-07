#!/usr/bin/env python3

import configparser
from pathlib import Path

def remember_date_load(app_path):
    try:
        config_file = Path(app_path)/"config.ini"
        if not config_file.exists():
            False

        config = configparser.ConfigParser()
        config.read(config_file)
        return config.getboolean('SETTINGS', 'clean_date', fallback=False)
    except Exception as e:
        print(e)
        return False

def load_hour_format(app_path):
    try:
        config_file = Path(app_path)/"config.ini"
        if not config_file.exists():
            return True

        config = configparser.ConfigParser()
        config.read(config_file)
        return config.getboolean('SETTINGS', 'hour_format', fallback=True)
    except Exception as e:
        print(e)
        return True

def save_hour_format(is_24h, app_path):
    try:
        config_file = Path(app_path)/"config.ini"
        config = configparser.ConfigParser()
        config.read(config_file, encoding="utf-8")
        if 'SETTINGS' not in config:
            config.add_section('SETTINGS')

        config.set('SETTINGS', 'hour_format', str(is_24h))
        with open(config_file, "w", encoding="utf-8") as f:
            config.write(f)
    except Exception as e:
        print(e)

def trial_autoload(app_path, check_val):
    try:
        config_file = Path(app_path)/"config.ini"
        config = configparser.ConfigParser()
        config.read(config_file, encoding="utf-8")
        if 'SETTINGS' not in config:
            config.add_section('SETTINGS')

        config.set('SETTINGS', 'clean_date', str(check_val))
        with open(config_file, "w", encoding="utf-8") as f:
            config.write(f)
    except Exception as e:
        print(e)