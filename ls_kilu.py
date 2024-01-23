import os


def main():
    path = os.getcwd()  # path of the current working directory
    dir_list = os.listdir(path)
    for list in dir_list:
        print(list, end=" ")
    print()


main()
