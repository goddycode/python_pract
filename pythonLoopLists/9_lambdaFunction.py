#!/usr/bin/python3
"""
This is script illustrate Lambda Function 
"""
import json


def mylambdafunc(n):
    return lambda a : a * n


x = mylambdafunc(3)
print(x(11))
