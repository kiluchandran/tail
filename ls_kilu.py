#!/usr/bin/env python3


import os
import sys
from termcolor import colored, cprint
import argparse


parser = argparse.ArgumentParser()
parser.add_argument(
    "-t", "--time", help="display files as per last updated time", action="store_true")
parser.add_argument(
    "-r", "--reverse", help="display files as per last updated time in reverse order", action="store_true")

args = parser.parse_args()


def sorted_by_modified_time(lists):
    lists.sort(key=os.path.getmtime)
    lists.reverse()
    return lists


def sorted_by_modified_time_reverse(lists):
    lists.sort(key=os.path.getmtime)
    return lists


def main():
    path = os.getcwd()  # path of the current working directory
    lists = os.listdir(path)
    lists.sort()
    if args.time and args.reverse:
        lists = sorted_by_modified_time_reverse(lists)
    if args.time:
        lists = sorted_by_modified_time(lists)
    if args.reverse:
        lists.reverse()
    for item in lists:
        if os.path.isdir(item):
            text = colored(item, 'blue')
        elif os.path.isfile(item):
            if os.access(item, os.X_OK):
                text = colored(item, 'green')
            else:
                text = colored(item, 'grey')
        print(text, end=" ")

    print()


main()
