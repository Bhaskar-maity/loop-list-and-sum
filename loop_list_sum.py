# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 16:51:24 2019

@author: user
"""

a=[]
n=int(input("Enter the length of list>>"))
for i in range(n):
    x=input("Enter element")
    a.append(x)
ra=a[::-1]
final=[]
for i in range(n):
  x=a[i]+ra[i]
  final.append(x)
for i in range(n):
  if i!=n-1:
      print(final[i],end=" ")
  else:
    print(final[i],end="")
      

 	