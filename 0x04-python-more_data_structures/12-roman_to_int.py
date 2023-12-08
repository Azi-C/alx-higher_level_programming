#!/usr/bin/python3
def roman_to_int(roman_string):
    if isinstance(roman_string, str) is False or roman_string is None:
        return 0
    total = 0
    new = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    for i, j in zip(roman_string, roman_string[1:]):
        if i not in new.keys():
            return 0
        elif new[i] >= new[j]:
            total += new[i]
        else:
            total -= new[i]
    total += new[roman_string[-1]]
    return total
