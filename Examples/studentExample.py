# -*- coding: utf-8 -*-
"""
Created on Wed Jan 29 17:04:45 2020

@author: trellis
"""

records={}
sum=0
avg={}
number=int(input("Enter the no. of students"))
for i in range(number):
    student={}
    name=input("Enter the student name")
    nsub=int(input("Enter the number of subjects"))
    for j in range(nsub):
        subname=input("Enter the name of subject{0}".format(j))
        marks=int(input("Enter the marks of {0}: ".format(subname)))
        student[subname]=marks
        sum=sum+marks
        
    average=sum/nsub
    avg[name]=average
    records[name]=student
print(records)
print(avg)

        