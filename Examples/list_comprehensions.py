# -*- coding: utf-8 -*-
"""
Created on Thu Jan 30 17:50:41 2020

@author: trellis
"""
#
#numbers=[1,2,3,4,5,6]
#
#squares=[number**2 for number in numbers]
#print(squares)
#
#
#text="Just to check the program"
#capital=[word.upper() for word in text.split()]
#print(capital)
#
#
#output=[]
#text=input("Enter the text")
#for x in text.split():
#    output.append((x,len(x)))
#print(output)
#
#answer={(x,len(x)) for x in text.split()}
#print(answer)

inch_measurement=(3,8,20)
cm_measurement=tuple([x*(2.5)for x in inch_measurement])
print(cm_measurement)



menu = [
    ["egg", "spam", "bacon"],
    ["egg", "sausage", "bacon"],
    ["egg", "spam"],
    ["egg", "bacon", "spam"],
    ["egg", "bacon", "sausage", "spam"],
    ["spam", "bacon", "sausage", "spam"],
    ["spam", "egg", "spam", "spam", "bacon", "spam"],
    ["spam", "egg", "sausage", "spam"],
    ["chicken", "chips"]
]
 

#for meal in menu:
#    if "spam" not in meal:
#        print(meal)
    
    
answer=[meal for meal in menu if "spam" in meal or "egg" in meal if not ("spam" in meal and "sausage" in meal) ]
print(answer)






