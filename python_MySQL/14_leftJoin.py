#!/usr/bin/python3
""" Script illustrating MySQL - Python connector
"""
import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="goddy",
    password="password",
    database="mydatabase"
)

mycursor = mydb.cursor()

sql = "SELECT \
users.name AS user, \
products.name AS favorite \
FROM users \
LEFT JOIN products ON users.fav = products.id"

mycursor.execute(sql)

data = mycursor.fetchall()

for x in data:
    print(x)
