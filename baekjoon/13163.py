import sys
input = lambda: sys.stdin.readline().strip()

def solution(s):
    s[0] = 'god'
    return ''.join(s)
    
n = int(input())
for _ in range(n):
    s = input().split()
    print(solution(s))
