#!/usr/bin/python3
""" """
import json


x = {"name": "Goddy", 
    "age": 36, 
    "city": "Nairobi"
}

#converting python into JSON
y = json.dumps(x)

#print the product of JSON string
print(y)
