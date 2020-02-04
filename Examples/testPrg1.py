# -*- coding: utf-8 -*-
"""
Created on Fri Jan 31 16:09:11 2020

@author: trellis
"""

n=int(input("Enter the number"))
for i in range(1,n+1):
    if(i%3==0):
        if(i%5==0):
            print(i,"fizz buzz")
        print(i,"fizz")
    elif(i%5==0):
        if(i%3==0):
            print(i,"fizz buzz")
        print(i,"buzz")
    else:
        print(i," ")
        
        
    