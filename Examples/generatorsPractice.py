# -*- coding: utf-8 -*-
"""
Created on Thu Jan 30 13:00:50 2020

@author: trellis

"""
def yielddunction():
    yield "firstTime"
    yield "secondTime"
    yield "thirdTime"


for val in yielddunction():
    print(val)
    
    
    
def square():
    i=1
    while True:
        yield i*i
        i+=1

for val in square():
    if val>100:
        break
    else:
        print(val,end=" ")
        
        


def simgen():
     yield "firstTime"
     yield "secondTime"
     yield "thirdTime"
    
x=simgen()
for i in range(3):
    print(next(x))
    
    
    
#def fibonaci(num):
#    a,b=0,1
#    while a<num:
#        yield a
#        a,b=b,a+b
#limit=int(input("Enter the limit"))
#x=fibonaci(limit)
#
#for i in fibonaci(limit):
#    print(i,end=" ")





def fib(limit):
    a=0
    b=1
    while True:
        yield a
        a,b = b,a+b
n = int(input("Enter the limit for fibonacci series"))
x = fib(n)
for i in range(n):
    print(next(x),end=' ')
    
    
    
    
    
def oddnum(limit):
    a=1
    while True:
        yield a 
        a+=2
num=int(input("Enter the range for odd numbers"))
x=oddnum(num)
for i in range(num):
    print(next(x),end=" ")