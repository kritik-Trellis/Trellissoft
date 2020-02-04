# -*- coding: utf-8 -*-
"""
Created on Fri Jan 31 16:31:53 2020

@author: trellis
"""

string=input("Enter the string")
def alphabet():
    ch=97
    alpha={}
    for i in range(1,27):
        alpha[chr(ch)]=i
        ch+=1
    return alpha
output=""
alpha=alphabet()
for s in string:
    if(s==" "):
        continue
    if(s.isalpha()==True):
        rep=str(alpha[s])
        output=output+rep+" "
        
print(output)

        