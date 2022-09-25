# -*- coding: utf-8 -*-
"""
Created on Sun Sep 25 17:36:18 2022

@author: JUNMIN LEE
"""

# Q7. 럭키 스트레이트


N = map(str, input())
N = [int(n) for n in N]

if len(N) % 2 != 0:
    print("N의 자리수는 항상 짝수 형태여야합니다.")
    
else:
    s = int(len(N)/2)
    
    left = N[0:s]
    right = N[s:]
    
    
    if sum(left) == sum(right):
        print("LUCKY")
        
    else:
        print("READY")