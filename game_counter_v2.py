# -*- coding: utf-8 -*-
"""
    ----
 -----------
- Level 314 -
 -----------
    ----

@author: Alexander Williams
date: Tue Feb  4 03:16:01 2020

"""
import math

def factorial(n):
    if n < 0:
        raise ValueError("simple factorial must pass values > 0")
        
    result = 1
    
    for x in range(2, n + 1):
        # print(result, " * ", x)
        result = result * x
        
    return result

def combination(N, k):
    return factorial(N) / (factorial(k) * factorial(N - k))

print(factorial(6))

print(math.factorial(6))

