# -*- coding: utf-8 -*-
"""
Created on Fri Jan 31 17:19:36 2020

@author: trellis
"""

binary=int(input("Enter the binary number"))

def dec_bin(binary):
    i=0
    decimal=0
    while(binary!=0):
        dec=binary%10
        decimal=decimal+dec*pow(2,i)
        binary=binary//10
        i+=1
    return decimal

decimal=dec_bin(binary)
print(decimal)