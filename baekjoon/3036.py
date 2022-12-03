from math import gcd
import sys
input = lambda: sys.stdin.readline().strip()

def solution(n, radius):
    arr = []
    r = radius[0]
    for i in range(1, n):
        numerator = gcd(r, radius[i])
        arr.append(f'{r//numerator}/{radius[i]//numerator}')
    return arr

n = int(input())
radius = list(map(int, input().split()))
print(*solution(n, radius), sep='\n')
