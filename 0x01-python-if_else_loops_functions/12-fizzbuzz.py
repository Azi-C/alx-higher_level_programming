#!/usr/bin/python
def fizzbuzz():
    for i in range(1,101):
        match i:
            case (i % 3) == 0:
                print("{}".format(i), end=' ')
            case (i % 3) == 0 and (i % 5) == 0:
                print("{}".format(i), end=' ')
            case _:
                print("{}".format(i), end =' ')
