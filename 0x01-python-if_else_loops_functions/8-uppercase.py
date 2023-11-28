#!/usr/bin/python3
def uppercase(str):
    for c in str:
        if c >= 97 and c <= 123:
            c = chr(ord(c) - 97 + 65)
        print("{}".format(c), end='')
    print()
