#!/usr/bin/python3
"""
script illustrate polymophysm which help in 
implementing various with same method as 
show below
"""


class Car:

    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def move(self):
        """ Move class"""
        print("Drive!")

class Boat:

    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
           
    def move(self):
        """ Move class"""
        print("Sail!")

class Plane: 
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def move(self):
        """ Move class"""
        print("Fly!")

"""These are instances of class Car, Boat and Plane"""
car1 = Car("Ford", "Mustang")
boat1 = Boat("Ibiza", "Touring 20")
plane1 = Plane("Boeing", "747")

for x in (car1, boat1, plane1):
    x.move()





