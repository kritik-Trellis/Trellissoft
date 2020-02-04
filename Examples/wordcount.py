# -*- coding: utf-8 -*-
"""
Created on Thu Jan 30 10:57:29 2020

@author: trellis
"""

def wordcount(string):
    count={}
    words=string.split()
    
    for word in words:
        if word in count :
            count[word] +=1
        else:
            count[word]=1
    return count
line=input("Enter the line")

print("Word count",wordcount(line))

            