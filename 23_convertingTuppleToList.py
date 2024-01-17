#!/usr/bin/python3
"""
This is a python tuple
"""
import json


def printTuple():
    global myTuple
    myTuple = ("apple", "banana", " cherry", "melberry", "mangoe")
    """printing full tupple list"""
    print(myTuple)


printTuple()

"""Converting a Tuple to list"""
x = list(myTuple)
x.remove("mangoe")
myTuple = tuple(x)
print(json.dumps(myTuple))
