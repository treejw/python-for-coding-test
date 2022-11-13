import sys
input = sys.stdin.readline

def solution(n, graph, del_node):
    def dfs(node):
        if not graph[node]:
            del graph[node]
            return
        for nxt in graph[node]:
            dfs(nxt)
        del graph[node]
        return 
    dfs(del_node)
    return sum([1 for v_set in graph.values() if not v_set-{del_node}])

n = int(input().strip())
node_parents = list(map(int, input().strip().split()))
graph = {node: set() for node in range(n)}
del_node = int(input().strip())
for child, parent in enumerate(node_parents):
    if parent == -1: continue
    graph[parent].add(child)
print(solution(n, graph, del_node))
