#!/usr/bin/python3
"""This script illustrate how to use a TypeError"""


x = "hello"

if not type(x) is int:
    raise TypeError("Only integers are allowed")
