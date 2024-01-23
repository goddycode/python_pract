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

mycursor.execute("CREATE TABLE IF NOT EXISTS products (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255)) AUTO_INCREMENT=154")

sql = "INSERT INTO products (name) VALUES (%s)"
data = [
    ('Chocolate Heaven',),
    ('Tasty Lemons',),
    ('Vanilla Dreams',),
    ('Yoghurt',),
    ('Fanta Orange',)
]

mycursor.executemany(sql, data)

mydb.commit()

print(mycursor.rowcount, "inserted")

