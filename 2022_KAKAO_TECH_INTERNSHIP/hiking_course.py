# https://school.programmers.co.kr/learn/courses/30/lessons/118669

from collections import defaultdict
from math import inf
from heapq import heappush, heappop

def dijkstra(start, costMap, graph, is_gate, is_summit):
    queue = []
    heappush(queue, [costMap[start], start])
    
    while queue:
        cur_cost, cur = heappop(queue)
        if costMap[cur] < cur_cost:
            continue
        for nxt, nxt_cost in graph[cur].items():
            cost = max(cur_cost, nxt_cost)
            if not is_gate[nxt] and cost < costMap[nxt]:
                costMap[nxt] = cost
                if not is_summit[nxt]:
                    heappush(queue, [cost, nxt])
    return costMap
    
def solution(n, paths, gates, summits):
    graph = defaultdict(lambda:defaultdict(int))
    for (i,j,w) in paths:
        graph[i][j] = w
        graph[j][i] = w
    
    is_gate = defaultdict(bool)
    costMap = {k:inf for k in range(1,n+1)}
    for i in gates:
        is_gate[i] = True
        costMap[i] = 0
        
    is_summit = defaultdict(bool)
    for i in summits:
        is_summit[i] = True
        
    for gate in gates:
        costMap = dijkstra(gate, costMap, graph, is_gate, is_summit)

    min_summit = min(summits, key=lambda i: [costMap[i], i])
    return [min_summit, costMap[min_summit]]
