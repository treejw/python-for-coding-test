from itertools import combinations

def solution(N, S, arr):
    cnt = 0
    for i in range(1, N+1):
        for case in combinations(arr, i):
            if sum(case) == S:
                cnt += 1
    return cnt

N, S = map(int, input().split())
arr = list(map(int, input().split()))
print(solution(N, S, arr))
