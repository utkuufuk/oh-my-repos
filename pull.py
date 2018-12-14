#!/usr/bin/env python3
from pathlib import Path
from subprocess import Popen, call, PIPE, STDOUT
import argparse
import json
import sys
import os

TIMEOUT_SECS = 15
CONFIG_PATH = str(Path.home()) + "/.oh-my-repos.json"

if __name__ == '__main__':
    # read configuration file
    try:
        config = json.load(open(CONFIG_PATH))
    except FileNotFoundError:
        print('Config file not found at', CONFIG_PATH + ', try reinstalling.', file=sys.stderr)
        sys.exit(1)

    # read program argument if specified
    parser = argparse.ArgumentParser()
    parser.add_argument('--dir', type=str, default=config['dir'], help='Root directory of Git repositories.')
    args = parser.parse_args()

    # remember the current directory
    initialDir = os.getcwd()

    # discover & register repositories
    repoDirs = [f.path for f in os.scandir(args.dir) if f.is_dir() and os.path.isdir(f.path + "/.git")]
    for repo in repoDirs:
        os.chdir(repo)
        call(['mr', 'register'], stderr=STDOUT, stdout = open(os.devnull, 'w'))

    # run myrepos command from user home directory
    os.chdir(str(Path.home()))
    process = Popen("mr -j{0} update".format(len(repoDirs)).split(), stdout=PIPE)
    try:
        output, error = process.communicate(timeout=TIMEOUT_SECS)
    except:
        process.kill()
        output, error = process.communicate()
    for line in output.splitlines():
        print(str(line)[2:-1])
    if error:
        print("Error:", error, file=sys.stderr)

    # go back to initial directory
    os.chdir(initialDir)