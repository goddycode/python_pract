#!/usr/bin/python3
"""
This is a python List
"""
import json


def printListForLoop():
    myList = ["melbbery", "apple", "oranges", "mango"]
    for _ in myList:
        print(json.dumps(_))


printListForLoop()
