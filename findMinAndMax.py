# 请使用迭代查找一个list中最小和最大值，并返回一个tuple
# -*- coding: utf-8 -*-
def findMinAndMax(L):
    if L == []:
        return None,None
    for i in L:
        if not isinstance(i, (int, float)):
            raise TypeError('must be int or float')
            
    min=max = L[0]
    for i in L[1:]:
        if i >= max:
            max = i
        if i <= min: 
            min = i
    return min,max