import os
import sys
from termcolor import colored, cprint


def main():
    path = os.getcwd()  # path of the current working directory
    lists = os.listdir(path)
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
