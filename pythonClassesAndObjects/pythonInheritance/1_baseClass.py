#!/usr/bin/python3
"""
This is class which is a blueprint of creating an object
"""


class Person:
    """This class has a property called x"""
    def __init__(self, fname, lname):
        """  """
        self.fname = fname
        self.lname = lname

    def printname(self):
        print(f"My first name is {self.fname} and second name is {self.lname}")


"""This is instance of class MyClass"""
p1 = Person("Goddy", "Odhis")
p1.printname()
