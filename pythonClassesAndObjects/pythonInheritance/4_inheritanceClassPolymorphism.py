#!/usr/bin/python3
"""
script illustrate Inheritance Class Polymophysm which
help in implementing various classes with same method as 
show below
"""


class Vehicle:

    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def move(self):
        """ Move class"""
        print("Move!")


class Car(Vehicle):
    pass


class Boat(Vehicle):
    def move(self):
        print("Sail")

           
class Plane(Vehicle):
    def move(self):
        """ Move class"""
        print("Fly")

"""These are instances of class Car, Boat and Plane"""
car1 = Car("Ford", "Mustang")
boat1 = Boat("Ibiza", "Touring 20")
plane1 = Plane("Boeing", "747")

for x in (car1, boat1, plane1):
    x.move()





