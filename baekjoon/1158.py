from collections import deque
import sys
input = lambda: sys.stdin.readline().strip()

def solution(n, k):
    ans = []
    queue = deque(map(str, range(1, n+1)))
    while queue:
        queue.rotate(-(k-1))
        ans.append(queue.popleft())
    return ans

n, k = map(int, input().split())
res = solution(n, k)
print(f"<{', '.join(res)}>")
