# -*- coding: utf-8 -*-
"""
Created on Fri Jan 31 16:19:52 2020

@author: trellis
"""

string=input("Enter the string")
new_str=""
for i in string:
    if(i.isalpha()==True):
        new_str=new_str+i
def reverse(string):
    string=string[::-1]
    return string
print("Reversed string with only alphabets: ",reverse(new_str))