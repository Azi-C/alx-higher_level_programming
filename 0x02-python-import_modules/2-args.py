#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    n = len(argv)
    if n == 1:
        print("0 argumrnts .")
    elif n == 2:
        print("{} argument:".format(n))
    else:
        print("{} arguments:".format(n))

    for i in range(1, n):
        print("{}: {}".format(i, argv[i]))
