#!/usr/bin/env python3
from pathlib import Path
from subprocess import Popen, call, PIPE, STDOUT
import argparse
import json
import sys
import os

CONCURRENT_JOBS = 5
TIMEOUT_SECS = 15
CONFIG_PATH = str(Path.home()) + "/.oh-my-repos.json"

if __name__ == '__main__':
    # read program arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('-d', '--dir', type=str, help='root directory of Git repositories')
    parser.add_argument('-s', '--save', action='store_true', help='whether to add input path to saved directories')
    args = parser.parse_args()

    # get saved directories from configuration file if any
    savedDirs = set()
    try:
        savedDirs = {s for s in json.load(open(CONFIG_PATH))['dirs'] if s != ""}
    except FileNotFoundError:
        print("Configuration file not found:", CONFIG_PATH)

    try:
        if args.dir == None:
            if args.save:
                raise UserWarning("--save flag can only be used along with the --dir argument")
            if len(savedDirs) == 0:
                raise UserWarning("Could not find any saved directories in {0}".format(CONFIG_PATH))
        else:
            # convert input directory to absolute path & add it to the set of retrieved directories
            inputDir = os.path.abspath(args.dir.replace("~", str(Path.home())))
            if not os.path.isdir(inputDir):
                raise UserWarning("Invalid directory: {0}".format(inputDir))
            savedDirs.add(inputDir)
            if args.save:
                # add the input directory to the existing set of saved directories in the configuration file
                with open(CONFIG_PATH, 'w', encoding='utf-8') as f:
                    json.dump({"dirs":list(savedDirs)}, f, indent=4, ensure_ascii=False)
                    print("Input directory appended to existing directories in configuration file:", inputDir)
    except UserWarning as w:
        print(str(w), "\n")
        parser.print_help()
        sys.exit(1)

    # delete .mrconfig if it exists
    try:
        os.remove(str(Path.home()) + "/.mrconfig")
    except OSError:
        pass

    # discover & register repositories
    for gitRoot in savedDirs:
        print("\nDiscovering repositories in", gitRoot)
        repoDirs = [f.path for f in os.scandir(gitRoot) if f.is_dir() and os.path.isdir(f.path + "/.git")]
        for repo in repoDirs:
            os.chdir(repo)
            call(['mr', 'register'], stderr=STDOUT, stdout = open(os.devnull, 'w'))

    # run myrepos command from user home directory
    os.chdir(str(Path.home()))
    process = Popen("mr -j{0} update".format(CONCURRENT_JOBS).split())
    try:
        process.communicate(timeout=TIMEOUT_SECS)
    except:
        process.kill()
        process.communicate()