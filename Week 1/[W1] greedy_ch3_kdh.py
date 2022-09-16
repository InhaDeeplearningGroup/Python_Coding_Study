# -*- coding: utf-8 -*-
"""
Created on Fri Sep 16 13:21:06 2022

@author: kdh
"""

# Exercise 3-1 (모험가 길드)
N = list(map(int, input().split()))[0]
data = list(map(int, input().split()))
count = 0

while True:

    data = sorted(data, reverse=True)
    if len(data) == 0:
        break
    print(data)
    fear_up = data[0]
    # fear_down = data[-1]
    
    a1, b1 = divmod(N, fear_up)
    print(a1, b1)
    # a2, b2 = divmod(N, fear_down)
    if a1 == 0:
        print("No more parties")
        break
    data = data[fear_up:]
    count = count + 1
    
print("\n # of party: ", count)



# Exercise 3-3 (문자열 뒤집기)
data = list(map(str, input().split()))[0]
data_sliced = list(data)
idn_list = []

for i in range(len(data_sliced)):
    
    if i == len(data_sliced)-1: break

    if data_sliced[i] != data_sliced[i+1]:
        # print("detected")
        idn_list.append(i+1)
        
print("\n # of trials: ", len(idn_list)//2)