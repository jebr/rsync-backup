#!/usr/bin/env python3

# Python program to backup directory for several days

import argparse
import datetime
import json
import random
import os
import subprocess
import sys

try:
    os.chdir(os.path.dirname(sys.argv[0]))
except Exception:
    pass


# Resource path bepalen
def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.environ.get("_MEIPASS2", os.path.abspath("."))
    # logging.info('Pyinstaller file location {}'.format(base_path))
    return os.path.join(base_path, relative_path)


parser = argparse.ArgumentParser(description='Python Rsync backup')

# Constants
FILTER_FILE = resource_path('rsync_filter.txt')
LOG_FILE = resource_path('rsync_backup.log')
CONFIG_FILE = resource_path('config.json')


def init_config():
    if os.path.exists(CONFIG_FILE):
        with open(CONFIG_FILE, "r") as config_file:
            config = json.load(config_file)
        global backup_days
        global backup_source
        global backup_destination
        backup_days = config["BACKUP_DAYS"]
        backup_source = config["BACKUP_SOURCE"]
        backup_destination = config["BACKUP_DESTINATION"]
        if (backup_days == "") or (backup_source == "") or (backup_destination == ""):
            print('Please add proper data to config file')
            exit()
        if not isinstance(backup_days, int):
            print("Add proper value to BACKUP_DAYS")
            exit()
        if not os.path.isdir(backup_source):
            print("Add valid source path to the config file")
            exit()
        if not os.path.isdir(backup_destination):
            print("Add valid destination path to the config file")
            exit()
    else:
        print('Configuration file is missing!')
        exit()


def clear_screen():
    subprocess.check_call(['clear'])


def rsync_backup():
    filter_file = f"--exclude-from={FILTER_FILE}"
    global backup_temp
    backup_temp = backup_destination + "/temp"
    rsync_command = ["rsync", "-zrlctq", "--stats", "--delete", "--no-o", "--no-t", "--no-g", "--no-perms",
                     "--omit-dir-times", "-K", "-L", filter_file, backup_source, backup_temp]
    try:
        subprocess.check_call(rsync_command)
        write_log("SUCCESS", f"Backup from {backup_source} to {backup_destination}")
    except Exception as e:
        write_log(f'ERROR', {e})


def write_log(error_type, message):
    date_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(LOG_FILE, 'a') as logfile:
        logfile.write(f'{date_time}:{error_type}:{message}\n')


def copy_backup():
    number = 0
    write_log("SUCCES", f"Backup gekopieerd naar {number}")


def main():
    clear_screen()
    init_config()
    rsync_backup()
    # parser.add_argument("-d", "--days", help="Create bakup for specific days",
    #                    metavar="", type=int)

    # args = parser.parse_args()
    # if args.days:
    #    init_config()
    # else:
    #    parser.print_help()


if __name__ == '__main__':
    main()
