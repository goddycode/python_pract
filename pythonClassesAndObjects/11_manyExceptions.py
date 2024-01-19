#!/usr/bin/python3
"""This is Exxeption Handling"""


try:
    print(x)
except NameError:
    print("Variable x is not defined")
except:
    print("Something else went wrong")
