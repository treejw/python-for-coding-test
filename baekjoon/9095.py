# https://www.acmicpc.net/problem/9095

from collections import defaultdict

dp = defaultdict(int)
dp[1] = 1
dp[2] = 2
dp[3] = 4

def func(n):
    global dp
    if n in dp:
        return dp[n]
    dp[n] = func(n-3) + func(n-2) + func(n-1)
    return dp[n]
        
T = int(input().strip())
query = [int(input().strip()) for _ in range(T)]
for n in query:
    print(func(n))


# dp[1] = 1  # 1 
# dp[2] = 2  # 1+1, 2 
# dp[3] = 4  # 1+1+1, 1+2, 2+1, 3  
# dp[4] = 7  # 1+3, 
             # 1+1+2, 2+2,
             # 1+1+1+1, 1+2+1, 2+1+1, 3+1
# dp[5] = 13 # 1+1+3, 2+3,
             # 1+1+1+2, 1+2+2, 2+1+2, 3+2,
             # 1+3+1, ...
