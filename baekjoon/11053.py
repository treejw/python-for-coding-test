import sys
input = sys.stdin.readline

def func(N, A):
    dp = [1]*N
    for cur in range(1, N):
        for prev in range(cur):
            if A[cur] > A[prev] and dp[cur] <= dp[prev]:
                dp[cur] = dp[prev] + 1
                # print(f'cur: {cur}, prev: {prev}, dp: {dp}')
    return max(dp)    

N = int(input().strip())
A = list(map(int, input().strip().split()))
print(func(N, A))    
