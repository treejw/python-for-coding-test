import sys
input = lambda: sys.stdin.readline().strip()

def concat(ar1, ar2, ar3):
    length = len(ar1)
    board = [''] * length
    for i in range(length):
        board[i] = ar1[i] + ar2[i] + ar3[i]
    return board

def func(n):
    if n == 1:
        return ['*']
    item = func(n//3)
    top_btm = concat(item, item, item)
    center = [' '*(n//3)]*(n//3)
    middle = concat(item, center, item)
    return top_btm + middle + top_btm

n = int(input())
print(*func(n), sep='\n')
