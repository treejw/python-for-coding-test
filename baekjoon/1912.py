import sys
input = sys.stdin.readline

def func(n, arr):
    dp = arr.copy()
    for i in range(1, n):
        if dp[i-1] > 0:
            dp[i] += dp[i-1]
        # print(f'i: {i}, dp: {dp}\n')
    return max(dp)

n = int(input().strip())
arr = list(map(int, input().strip().split()))
print(func(n, arr))
