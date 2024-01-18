import argparse


def print_last_lines(file_name, no_of_lines):
    with open(file_name, "r") as file1:
        lines = file1.readlines()
        last_lines = lines[-no_of_lines:]
        for line in last_lines:
            print(line.rstrip())


parser = argparse.ArgumentParser()
parser.add_argument("input_file")
args = parser.parse_args()


def main(argument):
    file_name = argument.input_file
    no_of_lines = 10
    print_last_lines(file_name, no_of_lines)


main(args)
