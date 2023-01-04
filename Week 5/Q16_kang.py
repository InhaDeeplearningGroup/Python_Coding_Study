from collections import deque
from copy import deepcopy
n, m = map(int, input().split())
data = [[0]*m for _ in range(n)]
temp = [[0]*m for _ in range(n)]

for i in range(n):
    row = list(map(int, input().split()))
    data[i] = row

#4가지 이동 방향
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

result = 0

# print(data)

def virus(x, y): #DFS로 바이러스 확산 함수 생성
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx >= 0 and nx < n and ny >= 0 and ny < m: #nx, ny : 인덱스 번호
            if temp[nx][ny] == 0: #바이러스가 퍼질 수 있으면
                temp[nx][ny] = 2 # 바이러스 배치
                virus(nx,ny) #재귀적으로 수행

def get_score():
    score = 0
    for i in range(n):
        for j in range(m):
            if temp[i][j] == 0:
                score+=1

    return score

count=0
def dfs(count):
    global result
    global temp
    # # 시간초과
    # i, j, k = 0,1,2
    # temp = deepcopy(data)
    # while not(k == n*m-1 and j == n*m-2 and i == n*m-3) :
    #
    #     x_1, y_1 = i // m, i % m
    #     x_2, y_2 = j // m, j % m
    #     x_3, y_3 = k // m, k % m
    #     if temp[x_1][y_1] == 0 and temp[x_2][y_2] == 0 and temp[x_3][y_3] == 0:
    #         temp[x_1][y_1] = temp[x_2][y_2] = temp[x_3][y_3] = 1
    #         for x in range(n):
    #             for y in range(m):
    #                 if temp[x][y] == 2:  # 바이러스 위치에서 확산 진행
    #                     virus(x, y)
    #
    #         result = max(result, get_score())
    #         temp = deepcopy(data)
    #
    #     # 아래보다 더오래걸림
    #     k += 1
    #     if k == n*m:
    #         j += 1
    #         if j == n*m - 1:
    #             i += 1
    #             j = i + 1
    #         k = j + 1
    #
    #
    # for i in range(n*m):
    #     for j in range(i+1, n*m):
    #         for k in range(j+1, n*m):
    #             x_1, y_1 = i // m, i % m
    #             x_2, y_2 = j // m, j % m
    #             x_3, y_3 = k // m, k % m
    #
    #             if temp[x_1][y_1] == 0 and temp[x_2][y_2] == 0 and temp[x_3][y_3] == 0:
    #                 temp[x_1][y_1] = temp[x_2][y_2] = temp[x_3][y_3] = 1
    #                 for x in range(n):
    #                     for y in range(m):
    #                         if temp[x][y] == 2:  # 바이러스 위치에서 확산 진행
    #                             virus(x, y)
    #
    #                 result = max(result, get_score())
    #                 temp = deepcopy(data)

    # 해설에서 울타리 세우는 법: dfs(count) 이용
    if count==3: #울타리가 세 개 설치된 경우
        temp = deepcopy(data)

        for i in range(n):
            for j in range(m):
                if temp[i][j] == 2: #바이러스 위치에서 확산 진행
                    virus(i, j)

        result = max(result, get_score())

        return
    for i in range(n): # 빈 공간에 울타리 설치
        for j in range(m):
            if data[i][j] == 0:
                data[i][j] = 1
                count +=1
                dfs(count)
                data[i][j] = 0
                count -=1


dfs(count)
print(result)
