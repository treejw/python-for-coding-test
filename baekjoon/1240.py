import sys
input = sys.stdin.readline
from math import inf
import heapq as hq

def solution(n, connection, n1, n2):
    global graph
    
    if n1==n2:
        return 0
    if graph[n1][n2] < inf:
        return graph[n1][n2]

    def dijkstra(start, dest):
        graph[start][start] = 0
        queue = []
        hq.heappush(queue, [0, start])
        while queue:
            dist, node = hq.heappop(queue)
            if graph[start][node] < dist:
                continue

            for nxt, nxt_dist in connection[node]:
                nxt_dist = dist + nxt_dist
                if nxt_dist <= graph[start][nxt]:
                    graph[start][nxt] = nxt_dist
                    graph[nxt][start] = nxt_dist
                    hq.heappush(queue, [nxt_dist, nxt])
        return graph[start][dest]
    return dijkstra(n1, n2)
            
n, m = map(int, input().strip().split())
connection = {node: set() for node in range(1,n+1)}
graph = [[inf]*(n+1) for _ in range(n+1)]
for _ in range(n-1):
    n1, n2, d = map(int, input().strip().split())
    graph[n1][n2] = d
    graph[n2][n1] = d
    connection[n1].add((n2, d))
    connection[n2].add((n1, d))

for _ in range(m):
    n1, n2 = map(int, input().strip().split())
    print(solution(n, connection, n1, n2))
