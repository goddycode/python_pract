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

List2 = ["samaki", "beef", "vege"]
"""Inserting an item at the end of the list"""
print(json.dumps(List2))
myList.extend(List2)

print(json.dumps(myList))
