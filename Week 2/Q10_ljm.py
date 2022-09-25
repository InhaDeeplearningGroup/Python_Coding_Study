# -*- coding: utf-8 -*-
"""
Created on Sun Sep 25 17:57:04 2022

@author: JUNMIN LEE
"""
def attach(x, y, M, key, big_lock):
    for i in range(M):
        for j in range(M):
            big_lock[x+i-1][y+j-1] += key[i][j]

def detach(x, y, M, key, big_lock):
    for i in range(M):
        for j in range(M):
            big_lock[x+i-1][y+j-1] -= key[i][j]

def rotation(key, degree):
    M = len(key)
    rotated_key = [ [0]*M for _ in range(M) ]
    if degree == '0':
        rotated_key = key
    elif degree == '90':    # 시계 방향
        for i in range(M):
            for j in range(M):
                rotated_key[M-j-1][i] = key[i][j]
    elif degree == '-90': # 반시계 방향
        for i in range(M):
            for j in range(M):
                rotated_key[i][j] = key[i][M-j-1]
    elif degree == '180':
        for i in range(M):
            for j in range(M):
                rotated_key[i][j] = key[M-i-1][M-j-1]
    return rotated_key

def check(board, M, N):
    for i in range(N):
        for j in range(N):
            if board[M+i-1][M+j-1] != 1:
                return False
    return True


def solution(key, lock):
    # 자물쇠
    N, M = len(lock), len(key)

    big_lock = [[0]*(N+2*N-2) for _ in range(N+2*N-2)]

    for i in range(N):
        for j in range(N):
            big_lock[M+i-1][M+j-1] = lock[i][j]

    degrees = ['0', '90', '-90', '180']

    for d in degrees:
        rotated_key = rotation(key, d)
        for x in range(0, M+N):
            for y in range(0, M+N):
                attach(x, y, M, rotated_key, big_lock)
                if check(big_lock, M, N):
                    print("check!")
                    return True
                detach(x, y, M, rotated_key, big_lock)


key = [[0, 0, 0],
       [1, 0, 0],
       [0, 1, 1]]

lock = [[1, 1, 1],
        [1, 1, 0],
        [1, 0, 1]]

answer = solution(key, lock)

print("answer: ", answer)