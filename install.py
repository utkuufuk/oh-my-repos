#!/usr/bin/env python3
import os
import json
from pathlib import Path
from shutil import copyfile
from subprocess import call, STDOUT

CONFIG_DIR = str(Path.home()) + '/.config/oh-my-repos'
config = {'dir':str(Path.home()) + '/Github'}
try:
    copyfile("./pull.py", "/usr/bin/pull")
    print("Script copied into /usr/bin/")
    call('chmod +x /usr/bin/pull'.split(), stderr=STDOUT, stdout = open(os.devnull, 'w')) == 0
    try:
        os.mkdir(CONFIG_DIR)
    except FileExistsError:
        pass
    with open(CONFIG_DIR + "/config.json", 'w', encoding='utf-8') as f:
        json.dump(config, f, indent=4, ensure_ascii=False)
        print("Configuration file created:", CONFIG_DIR + "/config.json")
    print("Installation successful.")
except PermissionError:
    print("Permission denied. Try running the script again with 'sudo'")