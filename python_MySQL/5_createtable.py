#!/usr/bin/python3
""" Script illustrate mysql - python connector
"""
import mysql.connector


mydb = mysql.connector.connect(host = "localhost", user = "goddy", password = "password", database ="mydatabase")

mycursor = mydb.cursor()

mycursor.execute("CREATE TABLE customer (Fname VARCHAR(255), Sname VARCHAR(255), age int)")
