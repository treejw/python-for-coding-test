import sys
input = sys.stdin.readline

def func(n, m, board):
    for sz in range(min(n, m), 1, -1):
        for r in range(n-sz+1):
            for c in range(m-sz+1):
                if len({board[r][c], board[r+sz-1][c], board[r][c+sz-1], board[r+sz-1][c+sz-1]}) == 1:
                    return sz**2
    return 1

n, m = map(int, input().strip().split())
board = [input().strip() for _ in range(n)]
print(func(n, m, board))
