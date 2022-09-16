# -*- coding: utf-8 -*-
"""
Created on Fri Sep 16 13:21:06 2022

@author: kdh
"""

# Exercise 2-1 (거스름돈)
n = 1260
count = 0

coin_types = [500, 100, 50, 10]

for coin in coin_types:
    count += n // coin
    n %= coin
    
print(count)


# Exercise 2-2 (큰 수의 법칙)
N, M, K = map(int, input().split())
data = list(map(int, input().split()))

sorted_data = sorted(data, reverse=True)
aa, bb = divmod(M, K)

print(sorted_data[0] * K * aa + sorted_data[1] * bb)



# Exercise 2-3 (숫자 카드 게임)
N, M = map(int, input().split())

result = 0
for i in range(N):
    data = list(map(int, input().split()))
    
    min_value = 10001
    for a in data:
        min_value = min(min_value, a)
    result = max(result, min_value)

print(result)



# Exercise 2-4 (1이 될 때까지)
N, K = map(int, input().split())
count = 0
while N != 1:
    if divmod(N, K)[1] != 0:
        N = N - 1
        count += 1
    else:
        N = N//K
        count += 1
    
print(count)