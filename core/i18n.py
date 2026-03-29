#!/usr/bin/env python3

import json
from dataclasses import dataclass

from setup.resources import resource_path

@dataclass(frozen=True)
class Language:
    name: str
    code: str

AVAILABLE_LANGUAGES = [
    Language("English", "en"),
    Language("Polski", "pl"),
    ]

class I18n:
    def __init__(self, language: str):
        self.language = language
        self.translations = self._load_translations(language)

    def _load_translations(self, language: str):
        path = resource_path(f'uma-tt-db/assets/i18n/{language}.json')
        #if not path.exists():
        with open(path, 'r', encoding='utf-8') as f:
            return json.load(f)

    def t(self, key):
        node = self.translations
        for part in key.split('.'):
            if not isinstance(node, dict) or part not in node:
                return f"[{key}]"
            node = node[part]
        if not isinstance(node, str):
            return f"[{key}]"
        return node

    def current_lang(self):
        code = self.language
        return code