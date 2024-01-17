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

myTupple = ("samaki", "beef", "vege")
"""Inserting an item at the end of the list"""
print(json.dumps(myTupple))
myList.extend(myTupple)

print(json.dumps(myList))
