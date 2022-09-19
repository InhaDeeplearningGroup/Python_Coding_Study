# -*- coding: utf-8 -*-
"""
Created on Fri Sep 16 17:10:09 2022

@author: PSJ
"""

n = int(input())
fear_levels = list(map(int, input().split()))

fear_levels.sort()

count = 0
while True:
    if len(fear_levels) == 0:
        break
    
    for _ in range(fear_levels[-1]):
        fear_levels.pop()
        if len(fear_levels) == 0:
            break
    count += 1
    
print(count)
        