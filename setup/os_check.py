#!/usr/bin/env python3

import platform

from core.close import close

def check_os():
    system = platform.system()
    if system in ('Linux', 'Windows'):
        print(f"OS detected: {system}")
        return system
    else:
        print(f">>> OS detected: {system}\n>>> Closing the program...")
        close()