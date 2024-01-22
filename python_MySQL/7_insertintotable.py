#!/usr/bin/python3
""" Script illustrate mysql - python connector
"""
import mysql.connector


mydb = mysql.connector.connect(host = "localhost", user = "goddy", password = "password", database ="mydatabase")

mycursor = mydb.cursor()

sql = "INSERT INTO customer (Fname, Sname, age) VALUES (%s, %s, %s)"
val = [
    ('Peter', 'John', 45),

    ('John', 'Paul', 43),
    ('Caroline', 'Jaoko', 45),
    ('Rose', 'Jack', 47),
    ('Carol', 'Willian', 20),
    ('Lilian', 'Akoth', 30),
    ('Rose', 'Auma', 24),
    ('Magret', 'Apondi', 45),
    ('Naomi', 'Wajiku', 30),
    ('Leah', 'Clera', 45),
    ('Gabril', 'Okath', 46),
    ('Wafula', 'Wakhungu', 32)
]
mycursor.executemany(sql, val)

mydb.commit()

print(mycursor.rowcount, "was inserted")
