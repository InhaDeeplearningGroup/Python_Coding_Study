# -*- coding: utf-8 -*-
"""
Created on Tue Dec 27 20:44:49 2022

@author: user
"""


# Q.24 (안테나)
n = int(input())
a = list(map(int, input().split()))
a.sort()

median_cost = a[ (n-1) // 2 ]
print(median_cost)


# Q.25 (실패율)
def solution(N, stages):
    
    answer = []
    length = len(stages)  # no. of users
    
    for i in range(1, N+1):
        
        cnt = stages.count(i)
        
        if length == 0:
            fail = 0
        else:
            fail = cnt / length
            
        answer.append((i, fail))
        length -= cnt
        
    answer = sorted(answer, key=lambda t: t[1], reverse=True)
    
    answer = [i[0] for i in answer]
    return answer