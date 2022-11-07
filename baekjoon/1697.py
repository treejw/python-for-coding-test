import sys
input = sys.stdin.readline
from collections import deque

def solution(n, k):
    if n >= k:
        return n-k

    queue = deque()
    queue.append((n,0))
    visited = {n}
    while queue:
        cur, t = queue.popleft()
        for x in [cur+1, cur*2, cur-1]:
            if x > 0 and x < 2*k and x not in visited:
                if x == k:
                    return t+1
                queue.append((x,t+1))
                visited.add(x)
        
n, k = map(int, input().strip().split())
print(solution(n, k))
