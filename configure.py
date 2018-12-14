#!/usr/bin/env python3
import sys
import json
from pathlib import Path

CONFIG_PATH = str(Path.home()) + "/.oh-my-repos.json"
print("Git root set:", sys.argv[1])
config = {'dir': sys.argv[1]}
with open(CONFIG_PATH, 'w', encoding='utf-8') as f:
    json.dump(config, f, indent=4, ensure_ascii=False)
    print("Configuration file created:", CONFIG_PATH)
print("Installation successful.")