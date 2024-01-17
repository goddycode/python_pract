#!/usr/bin/python3
"""
This is a python List
"""
import json


def printList():
    global myList
    myList = ["apple", "banana", " cherry", "Orange"]
    print(json.dumps(myList))

printList()

"""Inserting an item at the end of the list"""
myList.append("melberry")

print(json.dumps(myList))
