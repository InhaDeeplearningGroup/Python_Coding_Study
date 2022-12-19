# -*- coding: utf-8 -*-
"""
Created on Fri Sep 16 13:21:06 2022

@author: kdh
"""

# Q.16 Laboratory
def inspection(graph):
    extended_graph = []
    for j in range(n+2):
        if j == 0 or j == n+1:
            a = [0 for _ in range(n+2)]
            extended_graph.append(a)
        else:
            a = [0] + [value for _, value in enumerate(graph[j-1])] + [0]
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
    
    global stack, no_walls
    stack = 0
    no_walls = 3
    SOLUTION = ((1,0),(0,1),(3,5))
    
    extended_graph = inspection(graph)
    coordinate = candidate2(extended_graph)
    
    comb = list(itertools.combinations(coordinate, 3))  # total 6545
        
            
    # raster scanning
    score_list = []
    for k in range(len(comb)):
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
    

