import sys


def print_last_lines(file_name, no_of_lines):
    with open(file_name, "r") as file1:
        lines = file1.readlines()
        last_lines = lines[-no_of_lines:]
        for line in last_lines:
            print(line.rstrip())


def main():
    file_name = sys.argv[1]
    no_of_lines = 10
    print_last_lines(file_name, no_of_lines)


main()
