#!/usr/bin/python3
""" Script illustrate mysql - python connector
"""
import mysql.connector


mydb = mysql.connector.connect(host = "localhost", user = "goddy", password = "password", database ="mydatabase")

mycursor = mydb.cursor()

data = mycursor.execute("SELECT * FROM customer")

print(data)
