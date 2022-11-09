import sys
input = sys.stdin.readline
from itertools import permutations

def calc(arr, op):
    res = arr[0]
    for i in range(len(arr)-1):
        if op[i] == '+':
            res += arr[i+1]
        elif op[i] == '-':
            res -= arr[i+1]
        elif op[i] == '*':
            res *= arr[i+1]
        elif op[i] == '/':
            res = (-1) * (-res//arr[i+1]) if res < 0 else res//arr[i+1]
    return res

def solution(n, arr, op):
    maxi, mini = -1e10, 1e10
    for op_case in set(permutations(op)):
        res = calc(arr, op_case)
        maxi, mini = max(res, maxi), min(res, mini)
    return maxi, mini

n = int(input().strip())
arr = list(map(int, input().strip().split()))
opDict = dict()
opDict['+'], opDict['-'], opDict['*'], opDict['/'] = map(int, input().strip().split())
op = []
for k, v in opDict.items():        # op = ['+','+','-','*','/']
    op.extend([k]*v)
print(*solution(n, arr, op), sep='\n')
