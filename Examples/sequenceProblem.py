# -*- coding: utf-8 -*-
"""
Created on Thu Jan 30 11:19:51 2020

@author: trellis
"""

import timeit

#string=input()
setup="""\
string="abcdefghik"
j=1
c=0
tmp=[]
"""
stmt="""
for i in range(len(string)):
    
    if(ord(string[j])==ord(string[j-1])+1):
        j+=1
        if(j==len(string)):
            tmp.append(string[c:j])
            break
        continue
    
    
        
    else:
        tmp.append(string[c:j])
        c=j
        j+=1
        if(j==len(string)):
            tmp.append(string[j-1])
            break
print(tmp)
"""
            
print(timeit.timeit(stmt,setup,number=100))

        
    