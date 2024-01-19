#!/usr/bin/python3
"""
script illustrate the relationship betwn base and child class
"""


class Student(Person):
    """This is a child class"""
    

"""This is instance of class Student"""
st = Student("Lucky", "Akoth")
st.printname()
