#!/usr/bin/env python3

# Python program to backup directory for several days

import argparse
import json
import pyperclip
import random
import os


try:
    os.chdir(os.path.dirname(sys.argv[0]))
except Exception as e:
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
BACKUP_DAYS = 7
BACKUP_SOURCE = ''  # full path to source folder
BACKUP_DESTENATION = ''  # full path to destination
FILTER_FILE = resource_path('rsync_filter.txt')  # path to rsync_filter.txt
LOG_FILE = resource_path('rsync_backup.log')


def rsync_backup(source, location, days):
    pass


def main():
    parser.add_argument("-var", "--var", help="help text",
                        metavar="", type=int)

    args = parser.parse_args()
    if args.var:
        rsync_backup(args.var)
    else:
        parser.print_help()


if __name__ == '__main__':
    main()
