#!/usr/bin/python3
""" Script illustrate mysql - python connector
"""
import mysql.connector


mydb = mysql.connector.connect(host = "localhost", user = "goddy", password = "password")

mycursor = mydb.cursor()

mycursor.execute("CREATE DATABASE mydatabase")
