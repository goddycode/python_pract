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

"""Inserting an item in a list"""
myList.insert(3, "melberry")

print(json.dumps(myList))
