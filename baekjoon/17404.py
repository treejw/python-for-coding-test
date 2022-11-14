import sys
input = lambda: sys.stdin.readline().strip()
from collections import deque

def solution(n, dp):
    rgb = deque([0,1,2]) # r:0 g:1 b:2 
    for _ in range(3):
        c1,c2,c3 = rgb
        dp[c1][0][c2] = 1e9
        dp[c1][0][c3] = 1e9
        rgb.rotate()
        
    for i in range(1, n):
        for j in range(3):
            for _ in range(3):
                c1,c2,c3 = rgb
                dp[j][i][c1] += min(dp[j][i-1][c2], dp[j][i-1][c3])
                rgb.rotate()
                
    ans = 1e9
    for i in range(3):
        c1,c2,c3 = rgb
        res = min(dp[c1][-1][c2], dp[c1][-1][c3])
        ans = min(ans, res)
        rgb.rotate()
    return ans
    
n = int(input())
dp = []
for _ in range(n):
    dp.append(list(map(int, input().split())))
print(solution(n, [[row[:] for row in dp] for _ in range(3)]))
