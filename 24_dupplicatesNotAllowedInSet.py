#!/usr/bin/python3
"""
This is a python tuple
"""
import json


def printSet():
    global mySet
    mySet = {"apple", "banana", " cherry", "melberry", "mangoe"}
    """printing full tupple list"""
    print(json.dumps(mySet))


printSet()

