import sys
input = sys.stdin.readline
from math import comb

t = int(input().strip())
for _ in range(t):
    n, m = map(int, input().strip().split())
    print(comb(m,n))
