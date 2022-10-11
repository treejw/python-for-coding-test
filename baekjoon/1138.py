from itertools import permutations

def solution(N, arr):
    arr = [0] + arr
    for case in permutations(range(1,N+1), N):
        for i, h in enumerate(case):
            if arr[h] != len([1 for x in case[:i] if x>h]): 
                break
        else:
            return case

N = int(input())
arr = list(map(int, input().split()))
print(*solution(N, arr))
