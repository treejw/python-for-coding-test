# https://programmers.co.kr/learn/courses/30/lessons/12978
# 배달


from math import inf

def solution(N, road, K):
    graph = [[inf for _ in range(N+1)] for _ in range(N+1)]
        
    for r in road:
        a, b, c = r
        graph[a][b] = graph[b][a] = min(c, graph[a][b])
    
    for i in range(1, N+1):
        graph[i][i] = 0
        for a in range(1, N+1):
            for b in range(1, N+1):
                graph[a][b] = graph[b][a] = min(graph[a][b], graph[a][i]+graph[i][b])
    
    return len([True for i in range(1, N+1) if graph[1][i]<=K])
