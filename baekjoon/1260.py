from collections import deque, defaultdict
import sys
input = lambda: sys.stdin.readline().strip()
    
def dfs(cur, visited):
    global graph
    if len(visited) == len(graph):
        return visited
    for nxt in graph[cur]:
        if nxt not in visited:
            visited[nxt] = len(visited)+1
            visited = dfs(nxt, visited)
    return visited

def bfs(start, visited):
    global graph
    queue = deque([start])
    while queue:
        cur = queue.popleft()
        for nxt in graph[cur]:
            if nxt not in visited:
                queue.append(nxt)
                visited[nxt] = len(visited)+1
    return visited
    
def solution(n, v, graph):                
    visited = {v:1}
    dfs_visited = dfs(v, visited.copy())    # {3: 1, 1: 2, 2: 3, 5: 4, 4: 5}
    print(*sorted(dfs_visited.keys(), key=lambda k: dfs_visited[k]))
    bfs_visited = bfs(v, visited.copy())
    print(*sorted(bfs_visited.keys(), key=lambda k: bfs_visited[k]))

n, m, v = map(int, input().split())
graph = defaultdict(set)          
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].add(b)
    graph[b].add(a)
for key, value in graph.items():
    graph[key] = sorted(value)    # {5: [2, 4], 4: [3, 5], 2: [1, 5], 1: [2, 3], 3: [1, 4]})
solution(n, v, graph)
