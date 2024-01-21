import argparse
import time


def print_last_lines(file1, no_of_lines):
    lines = file1.readlines()
    last_lines = lines[-no_of_lines:]
    for line in last_lines:
        print(line.rstrip())


def follow(file1):
    while True:
        line = file1.readline()
        if not line:
            time.sleep(0.1)
            continue
        yield line


parser = argparse.ArgumentParser()
parser.add_argument("input_file")
parser.add_argument("-n", "--number", type=int,
                    help="display last n no of lines")
parser.add_argument("-f", "--follow", action="store_true",
                    help="display the last appended lines")
args = parser.parse_args()


def main(args):
    file_name = args.input_file
    file1 = open(file_name, "r")
    if args.number:
        no_of_lines = args.number
    else:
        no_of_lines = 10
    print_last_lines(file1, no_of_lines)

    if args.follow:
        for line in follow(file1):
            print(line)


main(args)
