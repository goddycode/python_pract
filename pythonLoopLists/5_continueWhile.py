#!/usr/bin/python3
"""
This is a python List
"""


def printListForLoop():
    myList = ["melbbery", "apple", "oranges", "mango"]
    i = 0
    while i < len(myList):
        if len(myList) == 1:
            continue
        print(i)
        i = i + 1


printListForLoop()
