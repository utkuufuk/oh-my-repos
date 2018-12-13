#!/usr/bin/env python3
import os
import json
from pathlib import Path
from shutil import copyfile
from subprocess import call, STDOUT

CONFIG_PATH = str(Path.home()) + '/.config/oh-my-repos/config.json'
config = {'dir':str(Path.home()) + '/Github'}
try:
    copyfile("./pull.py", "/usr/bin/pull")
    print("Script copied into /usr/bin/")
    call('chmod +x /usr/bin/pull'.split(), stderr=STDOUT, stdout = open(os.devnull, 'w')) == 0
    with open(CONFIG_PATH, 'w', encoding='utf-8') as f:
        json.dump(config, f, indent=4, ensure_ascii=False)
        print("Configuration file created:", CONFIG_PATH)
    print("Installation successful.")
except PermissionError:
    print("Permission denied. Try running the script again with 'sudo'")