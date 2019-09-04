#/usr/python
#_*_ coding:utf-8 _*_



import os

i = 1
while i <= 3:
    user = input("please enter user name:")
    pin = input("please enter your PIN:")
    if user != "admain" or pin != "123456":
        i += 1
        print ("please enter again")
    else:
        print ("welcome to login")
else:
    print("has been locaked")
    