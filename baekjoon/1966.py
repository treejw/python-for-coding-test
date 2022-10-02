# https://www.acmicpc.net/problem/1966

from collections import deque

def func(m, importance):                                       # importance = [1,2,3,4]
    queue = deque([(i,p) for i,p in enumerate(importance)])    # queue = deque([(0, 1), (1, 2), (2, 3), (3, 4)])
    importance.sort()

    n_printed = 0
    while queue:
        i, p  = queue.popleft()
        if p == importance[-1]:
            importance.pop()
            n_printed += 1
            if i == m:
                return n_printed
        else:
            queue.append((i,p))
                
T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    importance = list(map(int, input().split()))
    print(func(M, importance))
