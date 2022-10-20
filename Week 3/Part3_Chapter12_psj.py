#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct  2 22:07:50 2022

@author: PSJ

Part 3
Chapter 17
Q7. 럭키 스트레이트
Q10. 자물쇠와 열쇠
"""

import time

#%% Q7. 럭키 스트레이트

N = input()

start_time = time.time()

left_side = N[:int(len(N)/2)]
right_side = N[int(len(N)/2):]

sum_left_side = 0
for n in left_side:
    sum_left_side += int(n)

sum_right_side = 0
for n in right_side:
    sum_right_side += int(n)
    
if sum_left_side == sum_right_side:
    print("LUCKY")
else:
    print("READY")

end_time = time.time()
print(f"Runtime: {end_time - start_time:.5f}sec")
#%% Q10. 자물쇠와 열쇠


def solution(key, lock):
    """ 
    Key가 lock을 slide 하며 홈을 모두 채울 수 있는지 검사 
    """
    
    
    answer = True
    return answer

key = [[0, 0, 0], [1, 0, 0], [0, 1, 1]]
lock = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]

