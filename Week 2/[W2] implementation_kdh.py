# -*- coding: utf-8 -*-
"""
Created on Fri Sep 16 13:21:06 2022

@author: kdh
"""

# Exercise 4-1 (상하좌우)
size = map(int, input().split())
actions = list(map(str, input().split()))

x_loc, y_loc = 1, 1

for i in range(len(actions)):
    
    if actions[i] == 'L' and y_loc != 1:
        y_loc -= 1
    elif actions[i] == 'R' and y_loc != size:
        y_loc += 1
    elif actions[i] == 'U' and x_loc != 1:
        x_loc -= 1
    elif actions[i] == 'D' and x_loc != size:
        x_loc += 1

print('Final destination: ', (x_loc, y_loc))


# Exercise 4-2 (시각)
N = int(input())

cnt = 0
for i in range(N+1):
    for j in range(60):
        for k in range(60):
            if '3' in str(i) + str(j) + str(k):
                cnt +=1
                
print('# of 3 count is: ', cnt)


# Exercise 4-3 (왕실의 나이트)
# input_data = input()
# row = int(input_data[1])
# column = int(ord(input_data[0])) - int(ord('a')) + 1
location = str(input())

row_grid = [ '1',   '2',   '3',   '4',   '5',   '6',   '7',   '8' ]
col_grid = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']

row, col = location[1], location[0]
print(row, col)

a1 = [int(row)+2, (col_grid.index(col)+1)]
a2 = [int(row)-2, (col_grid.index(col)+1)]
a3 = [int(row), (col_grid.index(col)+1)+2]
a4 = [int(row), (col_grid.index(col)+1)-2]
# print(a1, a2, a3, a4)

b1 = [a1[0], a1[1]+1]
b2 = [a1[0], a1[1]-1]
b3 = [a2[0], a2[1]+1]
b4 = [a2[0], a2[1]-1]
b5 = [a3[0]+1, a3[1]]
b6 = [a3[0]-1, a3[1]]
b7 = [a4[0]+1, a4[1]]
b8 = [a4[0]-1, a4[1]]
destination = [b1, b2, b3, b4, b5, b6, b7, b8]
# print(b1, b2, b3, b4, b5, b6, b7, b8)

cnt = 0
for i in range(len(destination)):
    if 0 not in destination[i] and -1 not in destination[i] and -2 not in destination[i]:
        cnt += 1
print('Possible actions are: ', cnt)


# Exercise 4-4 (게임 개발)
N, M = map(int, input().split())

d = [[0] * M for _ in range(N)]
x, y, direction = map(int, input().split())
d[x][y] = 1
print(x, y, d)

array = []
for i in range(N):
    array.append(list(map(int, input().split())))
print(array)

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def turn_left():
    global direction
    direction -= 1
    if direction == -1: direction =3
    
    
# start game
cnt = 1
turn_time = 0
while True:
    turn_left()
    nx = x + dx[direction]
    ny = y + dy[direction]
    if d[nx][ny] == 0 and array[nx][ny] == 0:
        d[nx][ny] = 1
        x = nx
        y = ny
        cnt += 1
        turn_time = 0
        continue
    else:
        turn_time += 1
        
        
    if turn_time == 4:
        nx = x - dx[direction]
        ny = y - dy[direction]
        if array[nx][ny] == 0:
            x = nx
            y = ny
        else:
            break
        turn_time = 0
        
        
print(cnt)


#####################

# Q.7 Lucky Straight
score = int(input())
length = int(len(str(score))/2)

n1 = str(score)[:length]
n2 = str(score)[length:]

if sum([int(i) for i in n1]) == sum([int(i) for i in n2]):
    print("LUCKY")
else:
    print("READY")
    
    
# Q.10 Lock and Key
def rotate_key(a):
    n = len(a) # 행 길이 계산
    m = len(a[0]) # 열 길이 계산
    result = [[0] * n for _ in range(m)] # 결과 리스트
    for i in range(n):
        for j in range(m):
            result[j][n - i - 1] = a[i][j]
    return result


def validity_check(new_lock):
    lock_length = len(new_lock) // 3
    for i in range(lock_length, lock_length * 2):
        for j in range(lock_length, lock_length * 2):
            if new_lock[i][j] != 1:
                return False
    return True


def run():
    # key, lock = map(int, input().split())
    key = [[0,0,0],[1,0,0],[0,1,1]]
    lock = [[1,1,1],[1,1,0],[1,0,1]]
    
    n = len(lock)
    m = len(key)
    
    new_lock = [[0] * (n * 3) for _ in range(n * 3)]
    
    for i in range(n):
        for j in range(n):
            new_lock[i + n][j + n] = lock[i][j]
    print(new_lock)

    for rot in range(4):
        key = rotate_key(key)
        for x in range(n*2):
            for y in range(n*2):
                for i in range(m):
                    for j in range(m):
                        new_lock[x+i][y+j] += key[i][j]
                        
                if validity_check(new_lock) == True:
                    return True
                for i in range(m):
                    for j in range(m):
                        new_lock[x+i][y+j] -= key[i][j]
        return False

if __name__ == "__main__":
    result = run()
    print(result)
    
    








