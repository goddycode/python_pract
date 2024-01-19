#!/usr/bin/python3
"""This script illustrates the conversion JSON to 
python"""
import json



"""Here are some JSON data"""
x = '{"name": "Goddy", "age": 36, "city": "Nairobi"}'

""" parsing x"""
y = json.loads(x)

"""The result is python dictionary"""
print(y["age"])


