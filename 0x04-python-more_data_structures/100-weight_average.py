#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list is not None:
        w = sum(b for a, b in my_list)
        return (sum(a*b for a, b in my_list)/w) if w > 0 else 0
    return (0)
