#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 18 14:37:54 2022

@author: PSJ
"""

seq = input()

zero = 0
one = 0

if seq[0] == '1':
    zero += 1
else:
    one += 1

for i in range(len(seq)-1):
    if seq[i] != seq[i+1]:
        if seq[i+1] == '1':
            zero += 1
        else:
            one += 1
            
print(min(zero, one))