import sys
input = sys.stdin.readline

def func(N, A, B):
    S = [0]*N
    A.sort(reverse=True) 
    indexs = sorted(range(N), key=lambda idx: B[idx])
    for i, idx in enumerate(indexs):
        S[idx] = A[i]*B[idx]
    return sum(S)

N = int(input().strip())
A = list(map(int, input().strip().split()))
B = list(map(int, input().strip().split()))
print(func(N,A,B))
