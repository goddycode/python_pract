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

"""Changing the second and third item of the list"""
myList[1:3] = ["melberry"]

print(json.dumps(myList))
