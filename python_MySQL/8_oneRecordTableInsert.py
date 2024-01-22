#!/usr/bin/python3
"""Connecting to databse mydatabase and inserting a record
"""
import mysql.connector


mydb = mysql.connector.connect(
    host = "localhost",
    user = "goddy",
    password = "password",
    database = "mydatabase"
)

mycursor = mydb.cursor()

sql = "INSERT INTO customer (Fname, Sname, age) VALUES (%s, %s, %s)"
data = ["Maggy", "Wathongi", 32]

mycursor.execute(sql, data)

mydb.commit()

print("1 record added, ID:", mycursor.lastrowid)
