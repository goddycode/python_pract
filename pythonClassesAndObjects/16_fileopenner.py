#!/usr/bin/python3
"""This illustrate how to open file to demofile2.txt"""



f = open("demofile2.txt", "a")
f.write("Now the file has more content!")
f.close()

#Openning and Reading file after appending:
f = open("demofile2.txt", "r")
print(f.read())
