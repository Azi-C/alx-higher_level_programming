#!/usr/bin/python3
def remove_char_at(str, n):
    a = ''
    for i in str:
        if i != n:
            a = a + i
    return a;

