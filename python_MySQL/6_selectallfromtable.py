#!/usr/bin/python3
""" Script illustrate mysql - python connector
"""
import mysql.connector


mydb = mysql.connector.connect(host = "localhost", user = "goddy", password = "password", database ="mydatabase")

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM customer")

data = mycursor.fetchall()

for x in data:
    print(x)
