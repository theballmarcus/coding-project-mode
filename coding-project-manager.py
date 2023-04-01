#!/usr/bin/env python3
import argparse
import json
import os 
import subprocess

from util import dir_path, bprint
#Dev:
import traceback

config_name = "/home/mci/github/coding-project-mode/config.json"

def set_project_directory(args):
    config["project-directory"] = os.path.abspath(getattr(args, 'directory'))
    bprint("Updated project directory to:", config["project-directory"])

def open_vscode_in_project(args):
    try:
        output = subprocess.check_output(['code', config["project-directory"]])
        bprint("Launching visual studio code in", config["project-directory"])

    except subprocess.CalledProcessError as e:
        print('Command failed with return code', e.returncode)

def cd_in_project(args):
    print("cd " + config["project-directory"])
    #bprint("Changing directory to", config["project-directory"])


def main():
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers()

    set_project_directory_parser = subparsers.add_parser('set-project-directory', aliases=['spd'])
    set_project_directory_parser.add_argument('directory', help='Path to project directory', type=dir_path)
    set_project_directory_parser.set_defaults(func=set_project_directory)

    open_vscode_in_project_pasrser = subparsers.add_parser('open-vscode-in-project', aliases=['code'])
    open_vscode_in_project_pasrser.set_defaults(func=open_vscode_in_project)

    cd_in_project_pasrser = subparsers.add_parser('cd-in-project', aliases=['cd'])
    cd_in_project_pasrser.set_defaults(func=cd_in_project)

    args = parser.parse_args()
    args.func(args)

if __name__ == '__main__':
    global config

    if os.path.exists(config_name):
        with open(config_name, 'r') as f:
            config = json.load(f)
    else:
        with open(config_name, 'w') as f:
            json.dump({
                "project-directory" : ""
            }, f)
    try:
        main()
    except Exception as e:
        print(traceback.format_exc())

    with open(config_name, 'w') as f:
        json.dump(config, f)
