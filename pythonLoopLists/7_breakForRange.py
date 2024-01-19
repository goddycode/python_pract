#!/usr/bin/python3
"""
This is a python break, for loop, if else and range
implementation
"""

def printListForLoop():
    i = 0
    for i in range (6):
        if i == 3:
            break

        print(i)

    else:
        print("Finally finished!")

printListForLoop()
