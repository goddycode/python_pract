#!/usr/bin/python3
"""Selecting from the table with special condition """
import mysql.connector


mydb = mysql.connector.connect(
    host = "localhost",
    user = "goddy",
    password = "password",
    database = "mydatabase"
) 

mycursor = mydb.cursor()

sql = "SELECT * FROM customer WHERE age = %s"
age = (45, )

mycursor.execute(sql, age)

content = mycursor.fetchall()

for x in content:
    print(x)
