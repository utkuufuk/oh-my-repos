#!/usr/bin/env python3
from pathlib import Path
from subprocess import Popen, call, PIPE, STDOUT, TimeoutExpired
import argparse
import json
import sys
import os

TIMEOUT_SECS = 60
CONFIG_PATH = str(Path.home()) + "/.ohmyrepos.json"

def main():
    # read program arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('-d', '--dir', type=str, help='root directory of Git repositories')
    parser.add_argument('-s', '--save', action='store_true', help='whether to save input path')
    args = parser.parse_args()

    # get saved directories from configuration file if any
    savedPaths = set()
    try:
        savedPaths = {s for s in json.load(open(CONFIG_PATH))['dirs'] if s != ""}
    except FileNotFoundError:
        print("Configuration file not found:", CONFIG_PATH)

    try:
        if args.dir == None:
            if args.save:
                raise UserWarning("--save flag can only be used along with the --dir argument")
            if len(savedPaths) == 0:
                raise UserWarning("Could not find any saved directories in {0}".format(CONFIG_PATH))
        else:
            # convert input directory to absolute path & add it to the set of retrieved directories
            inputDir = os.path.abspath(args.dir.replace("~", str(Path.home())))
            if not os.path.isdir(inputDir):
                raise UserWarning("Invalid directory: {0}".format(inputDir))
            savedPaths.add(inputDir)
            if args.save:
                # add the input path to existing set of saved directories in the configuration file
                with open(CONFIG_PATH, 'w', encoding='utf-8') as f:
                    json.dump({"dirs":list(savedPaths)}, f, indent=4, ensure_ascii=False)
                    print("Input path saved in configuration file:", inputDir)
    except UserWarning as w:
        print(str(w), "\n")
        parser.print_help()
        return

    # delete .mrconfig if it exists
    try:
        os.remove(str(Path.home()) + "/.mrconfig")
    except OSError:
        pass

    # discover & register repositories
    for path in savedPaths:
        print("\nDiscovering repositories in", path)
        repos = [f.path for f in os.scandir(path) if f.is_dir() and os.path.isdir(f.path + "/.git")]
        for repo in repos:
            os.chdir(repo)
            call(['mr', 'register'], stderr=STDOUT, stdout = open(os.devnull, 'w'))

    # run myrepos command from user home directory
    os.chdir(str(Path.home()))
    process = Popen("mr -j{0} update".format(len(repos)).split())
    try:
        process.communicate(timeout=TIMEOUT_SECS)
    except TimeoutExpired:
        print("Process timed out.", file=sys.stderr)
        process.kill()
    except Exception as e:
        print(e, file=sys.stderr)
        process.kill()

if __name__ == '__main__':
    main()