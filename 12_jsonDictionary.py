#!/usr/bin/python3
"""
This is a python Dict
"""
import json


def printDict():
    global x
    x = {"Name" : "Goddy", "Profession": "Software Engineer", "County": "Kisii"}
    print(json.dumps(x, indent=3))



printDict()


print( x)
