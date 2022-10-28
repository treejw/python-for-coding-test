import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def func(n, graph):
    not_visited = set(graph.keys())
    
    def dfs(cur):
        for nxt in graph[cur]:
            if nxt in not_visited:
                not_visited.remove(nxt)
                dfs(nxt)

    cnt = 0
    while not_visited:
        node = not_visited.pop()
        dfs(node)
        cnt += 1
    return cnt

n, m = map(int, input().strip().split())
graph = {node: [] for node in range(1, n+1)}
for _ in range(m):
    u, v = map(int, input().strip().split())
    graph[u].append(v)
    graph[v].append(u)
print(func(n, graph))
