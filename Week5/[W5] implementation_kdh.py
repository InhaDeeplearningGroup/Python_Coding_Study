# -*- coding: utf-8 -*-
"""
Created on Fri Sep 16 13:21:06 2022

@author: kdh
"""

# Exercise 5-1 (Stack)
stack = []

stack.append(5)
stack.append(2)
stack.append(3)
stack.append(7)
stack.pop()
stack.append(1)
stack.append(4)
stack.pop()

print(stack)
print(stack[::-1])



# Exercise 5-2 (Queue)
from collections import deque

queue = deque()

queue.append(5)
queue.append(2)
queue.append(3)
queue.append(7)
queue.popleft()
queue.append(1)
queue.append(4)
queue.popleft()

print(queue)
queue.reverse()
print(queue)


# Exercise 5-4
def recursive_function(i):
    
    if i == 100:
        return
    print('at the {}-th recursive function, call {}-th recursive function.'.format(i,i+1))
    recursive_function(i+1)
    print('Terminate {}-th recursive function.'.format(i))
    
recursive_function(1)


# Exercise 5-5
def factorial_iterative(n):
    result = 1
    
    for i in range(1, n+1):
        result *= i
    return result


def factorial_recursive(n):
    if n <= 1:
        return 1
    return n * factorial_recursive(n-1)

print('Iterative result: ', factorial_iterative(5))
print('Recursive result: ', factorial_recursive(5))


# Exercise 5-6
INF = 9999999999999999999

graph = [
    [0,   5,   7],
    [7,   0, INF],
    [5, INF,   1]
]
print(graph)



# Exercise 5-7
graph = [[] for _ in range(3)]

graph[0].append((1, 7))
graph[0].append((2, 5))

graph[1].append((0, 7))

graph[2].append((0, 5))

print(graph)


# Exercise 5-8 & 5-9
from collections import deque

def dfs(graph, v, visited):
    visited[v] = True
    print(v, end=' ')
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)
            
def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True
    while queue:
        v = queue.popleft()
        print(v, end=' ')
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
            
graph = [
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8], 
    [1, 7]
]

visited = [False] * 9
dfs(graph, 1, visited)

visited = [False] * 9
bfs(graph, 1, visited)


# Exercise 5-10
n, m = map(int, input().split())  # vertical, horizontal

graph = []
for i in range(n):
    graph.append(list(map(int, input())))
    
def icecream(x, y):
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return False
    
    if graph[x][y] == 0:
        graph[x][y] = 1
        
        dfs(x-1,y)
        dfs(x,y-1)
        dfs(x+1,y)
        dfs(x,y+1)
        return True
    return False


result = 0
for i in range(n):
    for j in range(m):
        if dfs(i,j) == True:
            result += 1
            
print(result)


###########
###########
###########

# Q.16 Laboratory
def inspection(graph):
    extended_graph = []
    for j in range(n+2):
        if j == 0 or j == n+1:
            a = [0 for _ in range(n+2)]
            # print(a)
            extended_graph.append(a)
        else:
            a = [0] + [value for _, value in enumerate(graph[j-1])] + [0]
            # print(a)
            extended_graph.append(a)
    return extended_graph
    
    
def candidate(graph):
    offset = 1
    coordinate = []
    for x in range(offset,n+offset):
        for y in range(offset,m+offset):
                if graph[x-1][y] == 2 or graph[x][y-1] == 2 or graph[x+1][y] == 2 or graph[x][y+1] == 2:
                    if graph[x][y] != 1:
                        coordinate.append((x-1,y-1))
    return coordinate


def candidate2(graph):
    offset = 1
    coordinate = []
    for x in range(offset,n+offset):
        for y in range(offset,m+offset):
            if graph[x][y] == 0:
                coordinate.append((x-1,y-1))
    return coordinate
    


def build_walls(graph, coordinate, comb):
    
    # new_graph = graph.copy()
    # print(new_graph)
    
    for _, j in enumerate(comb):  # 1,2,3
        # print(j[0],j[1])
        graph[j[0]][j[1]] = 1
    return graph
            

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def virus(x, y):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx >= 0 and nx < n and ny >= 0 and ny < m:
            if new_graph[nx][ny] == 0:
                new_graph[nx][ny] = 2
                virus(nx, ny)
                
def get_score():
    score = 0
    for i in range(n):
        for j in range(m):
            if new_graph[i][j] == 0:
                score += 1
    return score


if __name__ == "__main__":
    
    n, m = map(int, input().split())  # vertical, horizontal
    
    graph = []
    for i in range(n):
        graph.append(list(map(int, input())))

    
    import itertools
    import copy
    from tqdm import tqdm
    
    global stack, no_walls
    stack = 0
    no_walls = 3
    SOLUTION = ((1,0),(0,1),(3,5))
    
    extended_graph = inspection(graph)
    coordinate = candidate2(extended_graph)
    
    comb = list(itertools.combinations(coordinate, 3))  # total 6545
        
            
    # raster scanning
    score_list = []
    for k in tqdm(range(len(comb))):
        new_graph = copy.deepcopy(graph)
        new_graph = build_walls(new_graph, coordinate, comb[k])
        # print(new_graph)
    
        for i in range(n):
            for j in range(m):
                if new_graph[i][j] == 2:
                    virus(i,j)
        score_list.append(get_score())
        
    print("\n")
    print(max(score_list))
    

