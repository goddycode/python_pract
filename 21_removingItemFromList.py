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

"""Removing an Item from a specific item"""
myList.pop(3)

print(json.dumps(myList))
