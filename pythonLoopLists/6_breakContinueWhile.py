#!/usr/bin/python3
"""
This is a python List
"""


def printListForLoop():
    i = 0
    j = 0
    while i < 6:
        i = i + 1

        if i == 3:
            continue

        print(i)

printListForLoop()
