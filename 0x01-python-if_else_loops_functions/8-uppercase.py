#!/usr/bin/python3
# Author - Ozonah Favour
def uppercase(str):
    for c in str:
        if ord(c) >= 97 and ord(c) <= 122:
            print(chr(ord(c) - 32), end="")
        else:
            print(c, end="")
    print()
