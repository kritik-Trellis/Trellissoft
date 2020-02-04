# -*- coding: utf-8 -*-
"""
Created on Thu Jan 30 10:39:11 2020

@author: trellis
"""
import math
n=int(input("Enter the number of values you want to enter"))
values=[int(input("Enter the values")) for i in range(n)]

def checkPrime(num):
    for i in range(2,int(math.sqrt(num))+1):
        if(num%i==0):
            return False
    return True
prime=[]
for i in values:
    ret=checkPrime(i)
    if ret==True:
        prime.append(i)
print(prime)
        
    