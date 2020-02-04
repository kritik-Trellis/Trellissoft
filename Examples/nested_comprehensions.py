# -*- coding: utf-8 -*-
"""
Created on Fri Jan 31 12:29:00 2020

@author: trellis
"""

breads=["naan","tawa roti","tandoori roti"]
decorations=["Ghee","Butter"]
#for bread in breads:
#    for decoration in decorations:
#        print(bread,decoration)


for combination in [(bread,decoration) for bread in breads for decoration in decorations]:
    print(combination)
print("*"*40)
for nest_combination in [[(bread,decoration) for bread in breads] for decoration in decorations]:
    print(nest_combination)
    
print("*"*40)
for anoth_nest_combination in [[(bread,decoration) for decoration in decorations] for bread in breads]:
    print(anoth_nest_combination)
    


#challenge Problem
    
    
for i in range(1,11):
    for j in range(1,11):
        print(i,i*j,end="||")
    print()
    
    
    
for table in [(i,i*j)for i in  range(1,11) for j in range(1,11)]:
    print(table)



