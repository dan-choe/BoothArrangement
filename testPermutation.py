# -*- coding: utf-8 -*-
"""
Created on Tue Sep 19 17:12:18 2017

@author: danna
"""

def permutation(arr):
    if not len(arr):
        return []
    if len(arr) == 1:
        return [arr]
 
    l = []
    for i in range(len(arr)):
       m = arr[i]
       remLst = arr[:i] + arr[i+1:]
       for p in permutation(remLst):
           l.append([m] + p)
    return l

result = permutation([1,2,3])

for item in result:
    print(item)