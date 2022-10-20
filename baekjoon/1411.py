from math import comb
from collections import Counter
import sys
input = sys.stdin.readline

def trans(string):
    for i, s in enumerate(string):
        string = string.replace(s, str(i))
    return string

def func(n, arr):
    arr = list(map(lambda x: trans(x), arr))
    cnter = Counter(arr)
    answer = 0
    for v in cnter.values():
        if v == 1: continue
        answer += comb(v, 2)
    return answer

n = int(input().strip())
arr = [input().strip() for _ in range(n)]
print(func(n, arr))
