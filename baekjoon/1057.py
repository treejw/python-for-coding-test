# https://www.acmicpc.net/problem/1057

def func(n, a, b):
    cnt = 0
    while a != b:
        a -= a//2
        b -= b//2
        cnt += 1
    return cnt

N, a, b = map(int, input().split())
print(func(N, a, b))
