#!/usr/bin/python3
def remove_char_at(str, n):
    a = ''
    for i in str:
        if ord(i) != ord(n):
            a = a + i
    return a

