#!/usr/bin/python3
"""This is Exception Handling"""


try:
    print("Hello world")
except NameError:
    print("Variable 'Hello world' is not defined")
except:
    print("Something else went wrong")
else:
    print("Nothing went wrong")
