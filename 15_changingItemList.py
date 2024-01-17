#!/usr/bin/python3
"""
This is a python List
"""
import json


def printList():
    global myList
    myList = ["apple", "banana", " cherry", "Orange"]

printList()

"""Changing the range of Items"""
myList[1:3] = ["mangoes", "melberry"]

print(json.dumps(myList))
