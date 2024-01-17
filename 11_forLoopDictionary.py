#!/usr/bin/python3
"""
This is a python Dict
"""


def printDict():
    global x
    x = {"Name" : "Goddy", "Profession": "Software Engineer", "County": "Kisii"}
    for key, value in x.items():
        print(f'{key}: {value}')



printDict()


print( x)
