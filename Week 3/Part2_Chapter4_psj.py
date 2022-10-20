# -*- coding: utf-8 -*-
"""
Created on Fri Sep 30 20:03:35 2022

@author: PSJ
"""

import time

#%% [Part 2] Chapter 4. Example 4-1. 상하좌우

num_grid = int(input()) # (ex) 5
plans = input().split() # (ex) R R R U D D

start_time = time.time()
start_position = [1, 1]
for move in plans:
    if move == "L":     # (a, b) -> (a, b-1)
        start_position[1] -= 1 if start_position[1] > 1 else 0
    elif move == "R":   # (a, b) -> (a, b+1)
        start_position[1] += 1 if start_position[1] < num_grid else 0
    elif move == "U":   # (a, b) -> (a-1, b)
        start_position[0] -= 1 if start_position[0] > 1 else 0
    elif move == "D":   # (a, b) -> (a+1, b)
        start_position[0] += 1 if start_position[0] < num_grid else 0
    else:
        raise ValueError("Incorrect direction.")
        exit
end_time = time.time()
print(start_position[0], start_position[1])
print(f"time: {end_time - start_time:.5f} sec")


#%% [Part 2] Chapter 4. Example 4-2. 시각

N = int(input())

start_time = time.time()

count = 0
for i in range(N + 1):
    for j in range(60):
        for k in range(60):
            if '3' in str(i) + str(j) + str(k):
                count+=1
    
end_time = time.time()
print(count)
print(f"time: {end_time - start_time:.5f} sec")


#%% [Part 2] Chapter 4. 2. 왕실의 나이트

position = input()

position_dict = {"a":1, "b":2, "c":3, "d":4,
                 "e":5, "f":6, "g":7, "h":8}

current_position = [position_dict[position[0]], int(position[1])] # (ex) 'a1' -> [1, 1]

count = 0

# Check left and right
if current_position[0] >= 3 and current_position[0] <= 6:
    count += 2 if current_position[1] == 1 or current_position[1] == 8 else 4
else:
    count += 1 if current_position[1] == 1 or current_position[1] == 8 else 2

# Check up and down
if current_position[1] >= 3 and current_position[1] <= 6: 
    count += 2 if current_position[0] == 1 or current_position[0] == 8 else 4
else:
    count += 1 if current_position[0] == 1 or current_position[0] == 8 else 2    

print(count)

#%% [Part 2] Chapyer 4. 3. 게임 개발

N, M = map(int, input().split())
A, B, d= map(int, input().split())

directions = [0, 1, 2, 3] # [N, E, S, W]
maps = []
for _ in range(N):
    each_row = list(map(int, input().split())) # [1, 1, 1, 1]
    assert len(each_row) == M
    maps.append(each_row)

# 육지 0, 바다 1, 가본 칸 -1
stop_sign = False
step_count = 0
turn_count = 0
while not stop_sign:
    # 현재 위치를 가본 칸으로 설정
    maps[A][B] = -1
    
    ## 방향이 북쪽일 경우,
    if d == 0:
        # 4번째 회전했다면, 뒤 (남쪽)로 한 칸
        if turn_count == 4:
            turn_count = 0
            A += 1
            # 바다라면 움직임을 멈춤
            if maps[A][B] == 1:
                break
            step_count += 1
        # 4번 이하의 회전이며, 앞이 비었다면 서쪽으로 전진.
        else:
            d = directions[d-1] # 서쪽으로 회전
            turn_count += 1
            if maps[A][B-1] == 0:
                turn_count = 0
                B -= 1
                step_count += 1
        
        
        
    ## 동쪽일 경우,
    elif d == 1:
        # 4번째 회전했다면, 뒤 (서쪽)로 한 칸
        if turn_count == 4:
            turn_count = 0
            B -= 1
            # 바다라면 움직임을 멈춤
            if maps[A][B] == 1:
                break
            step_count += 1
            
        # 4번 이하의 회전이며, 앞이 비었다면 북쪽으로 전진.
        else:
            d = directions[d-1] # 북쪽으로 회전
            turn_count += 1
            if maps[A-1][B] == 0:
                turn_count = 0
                A -= 1
                step_count += 1
        
    ## 남쪽일 경우,
    elif d == 2:
        # 4번째 회전했다면, 뒤 (북쪽)으로 한 칸
        if turn_count == 4:
            turn_count = 0
            A -= 1
            # 바다라면 움직임을 멈춤
            if maps[A][B] == 1:
                break
            step_count += 1
        
        # 4번 이하의 회전이며, 앞이 비었다면 동쪽으로 전진
        else:
            d = directions[d-1] # 동쪽으로 회전
            turn_count += 1
            if maps[A][B+1] == 0:
                turn_count = 0
                B += 1
                step_count += 1
        
        
        
        
    ## 서쪽일 경우,
    elif d == 3:
        # 4번째 회전했다면, 뒤 (동쪽)으로 한 칸
        if turn_count == 4:
            turn_count = 0
            A += 1
            # 바다라면 움직임을 멈춤
            if maps[A][B] == 1:
                break
            step_count += 1
        
        # 4번 이하의 회전이며, 앞이 비었다면 남쪽으로 전진
        else:
            d = directions[d-1] # 남쪽으로 회전
            turn_count += 1
            if maps[A+1][B] == 0:
                turn_count = 0
                A += 1
                step_count += 1
        
print(step_count)
