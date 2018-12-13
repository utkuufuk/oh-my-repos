#!/usr/bin/env python3
from pathlib import Path
from subprocess import Popen, call, PIPE, STDOUT
import argparse
import json
import sys
import os

TIMEOUT_SECS = 15
CONFIG_PATH = str(Path.home()) + '/.config/oh-my-repos/config.json'
MR_CONFIG_PATH = str(Path.home()) + '/.mrconfig'

def isGitDir(path):
    return call(['git', '-C', path, 'status'], stderr=STDOUT, stdout = open(os.devnull, 'w')) == 0

def getRemote(path):
    process = Popen("git -C {0} remote -v".format(path).split(), stdout=PIPE)
    try:
        output, error = process.communicate(timeout=TIMEOUT_SECS)
        if error:
            raise Exception(error)
    except:
        process.kill()
        output, error = process.communicate()
    output = str(output)
    return output[output.find("git@"):output.find(" (fetch)")]

if __name__ == '__main__':
    try:
        config = json.load(open(CONFIG_PATH))
    except FileNotFoundError:
        print('Configuration file not found.', file=sys.stderr)
        sys.exit(1)

    parser = argparse.ArgumentParser()
    parser.add_argument('--dir', type=str, default=config['dir'], help='Root directory of Git repositories.')
    args = parser.parse_args()
    repoDirs = [f.path for f in os.scandir(args.dir) if f.is_dir() and isGitDir(f.path)]

    # populate .mrconfig file with local repos
    with open(MR_CONFIG_PATH, 'w', encoding='utf-8') as f:
        for repo in repoDirs:
            name = repo.replace(str(Path.home()), "")[1:]
            f.write("\n[{0}]\ncheckout = git clone '{1}' '{2}'\n".format(name, getRemote(repo), name[(name.find("/")) + 1:]))

    # temporarily change working directory to user home
    initialDir = os.getcwd()
    os.chdir(str(Path.home()))

    # run myrepos command
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