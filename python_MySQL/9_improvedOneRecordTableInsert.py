#!/usr/bin/python3
"""Script which connect to database and insert a 
record"""
import mysql.connector

try:
    mydb = mysql.connector.connect(
        host="localhost",
        user="goddy",
        password="password",
        database="mydatabase"
    )

    mycursor = mydb.cursor()

    sql = "INSERT INTO customer (Fname, Sname, age) VALUES (%s, %s, %s)"
    data = ("Caren", "Akinyi", 24)

    mycursor.execute(sql, data)

    mydb.commit()

    print("1 record added, ID: ", mycursor.lastrowid)

except mysql.connector.Error as err:
    print("Error:", err)

finally:
    if mydb.is_connected():
        mycursor.close()
        mydb.close()
        print("MySQl connection closed")
