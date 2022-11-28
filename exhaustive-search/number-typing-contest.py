from collections import defaultdict
from math import inf
    
def solution(numbers):
    phone = [[1,2,3], [4,5,6], [7,8,9], [10,0,11]]  # *: 10, #: 11

    dirx = [1, 0,  1,1]
    diry = [0, 1, -1,1]
    cost = [2, 2,  3,3]
    
    # costMap
    costMap = [[inf]*12 for _ in range(12)]
    for r in range(4):
        for c in range(3):
            cur = phone[r][c]
            costMap[cur][cur] = 1
            for dx, dy, w in zip(dirx, diry, cost):
                nr, nc = r+dx, c+dy
                if 0<=nr<4 and 0<=nc<3:
                    nxt = phone[nr][nc]
                    costMap[cur][nxt] = w
                    costMap[nxt][cur] = w
    # i에서 j까지 가는 최소 비용 (floyd warshall)
    for k in range(12):
        for i in range(12):
            for j in range(12):
                if i==j: continue
                costMap[i][j] = min(costMap[i][j], costMap[i][k]+costMap[k][j])
                costMap[j][i] = costMap[i][j]
    
    prev = {(4,6): 0}   # (kL, kR): cost
    for n in numbers:
        n = int(n)
        new = defaultdict(lambda:inf)
        for (kL,kR), weight in prev.items():
            if n != kR:
                new[(n,kR)] = min(new[(n,kR)], weight+costMap[kL][n])   # left
            if n != kL:
                new[(kL,n)] = min(new[(kL,n)], weight+costMap[kR][n])   # right
        prev = new
    return min(prev.values())
