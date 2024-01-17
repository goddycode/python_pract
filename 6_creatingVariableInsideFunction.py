#!/usr/bin/python3
"""
Create a variable outside of a function, and use it
 inside the function
"""

x = "awesome"


def myfunc():
    x = "fantastic"
    print("Python is "+x)


myfunc()


print("Python is "+x)
