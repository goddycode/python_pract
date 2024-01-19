#!/usr/bin/python3
"""
This is class which is a blueprint of creating an object
"""


class Person:
    """A class to represent a person with a name and age"""

    def __init__(self, name, age):
        """
        Initialized a Person Object.

        Parameters:
        - name (str): The name of Person
        - age (int): The age of Person
        """

        self.name = name
        self.age = age

@property
def name(self):
    """Getter method for retieving the name"""
    return self._name

@property
def age(self):
    """Getter method for retrieving age"""
    return self._age

@name.setter
def name(self, new_name):
    """Setter method for updating name"""
    self.__name = new_name

@age.setter
def age(self, new_age):
    """Setter method for updating age"""
    self.__age = new_age

    def myfunc(self):
        """Object method"""
        print(f"My name is {p1.name} and I am {p1.age} old")

"""This is function's object"""
p1 = Person("Goddy", 36)
p1.myfunc()
