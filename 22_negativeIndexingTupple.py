#!/usr/bin/python3
"""
This is a python tuple
"""


def printTupple():
    global myTupple
    myTupple = ("apple", "banana", " cherry", "melberry", "mangoe")
    """printing full tupple list"""
    print(myTupple)


printTupple()

"""Negetaive indexing means printing items starting from last item"""
print(myTupple[-1:-4])
