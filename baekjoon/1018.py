import sys
input = sys.stdin.readline

def cnt_diff(row, dest):
    return sum([1 for c, d in zip(row,dest) if c!=d])

def func(N, M, board):
    mini = 1e9
    for r in range(N-7):
        for c in range(M-7):
            start_B = 0
            start_W = 0
            for idx, ri in enumerate(range(r, r+8)):
                row = board[ri][c:c+8]
                start_B += cnt_diff(row,'BWBWBWBW') if idx%2==0 else cnt_diff(row,'WBWBWBWB')
                start_W += cnt_diff(row,'WBWBWBWB') if idx%2==0 else cnt_diff(row,'BWBWBWBW')
            mini = min(mini, start_B, start_W)
    return mini

N, M = map(int, input().strip().split())
board = [input().strip() for _ in range(N)]
print(func(N, M, board))
