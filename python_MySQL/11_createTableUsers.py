#!/usr/bin/python3
""" Script illustrate mysql - python connector
"""
import mysql.connector


mydb = mysql.connector.connect(host = "localhost", user = "goddy", password = "password", database ="mydatabase")

mycursor = mydb.cursor()


mycursor.execute("CREATE TABLE IF NOT EXISTS users (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), fav INT)")


sql = "INSERT INTO users (name, fav) VALUES (%s, %s)"
data = [
    ('John', 154),
    ('Peter', 154),
    ('Amy', 155),
    ('Hannah', 155),
    ('Michael', 155)
]

mycursor.executemany(sql, data)

mydb.commit()

print(mycursor.rowcount, "inserted")
