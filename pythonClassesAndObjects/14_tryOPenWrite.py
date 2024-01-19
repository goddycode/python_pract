#!/usr/bin/python3
"""This script tries to open and write a file"""



try:
    f = opne("demofile.txt")
    try:
        f.write("Lorum Ipsum")
    except:
        print("Something went wrong when writting to the file")
    finally:
        f.close()

except:
    print("Something went wrong when opening the file")
