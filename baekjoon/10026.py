import sys
sys.setrecursionlimit(10**5)
input = lambda: sys.stdin.readline().strip()

def solution(n, board):
    move = [(-1,0),(1,0),(0,-1),(0,1)]
    
    def dfs(item, r, c, flag=False):
        for dx, dy in move:
            nr, nc = r+dx, c+dy
            if 0<=nr<n and 0<=nc<n and board[nr][nc]==item:
                if not flag:
                    board[nr][nc] = 1 if board[nr][nc] == 'B' else 2
                else:
                    board[nr][nc] = 0
                dfs(item, nr, nc, flag)
    cnt_x = 0
    for r in range(n):
        for c in range(n):
            if type(board[r][c]) == str:
                item = board[r][c]
                board[r][c] = 1 if board[r][c] == 'B' else 2
                dfs(item, r,c)
                cnt_x += 1
    cnt_o = 0
    for r in range(n):
        for c in range(n):
            if board[r][c] != 0:
                item = board[r][c]
                board[r][c] = 0
                dfs(item, r,c, flag=True)
                cnt_o += 1
    return cnt_x, cnt_o
    
n = int(input())
board = [list(input()) for _ in range(n)]
print(*solution(n, board))

# ['R', 'R', 'R', 'B', 'B']    [2, 2, 2, 1, 1]    [0, 0, 0, 0, 0]
# ['G', 'G', 'B', 'B', 'B']    [2, 2, 1, 1, 1]    [0, 0, 0, 0, 0]
# ['B', 'B', 'B', 'R', 'R']    [1, 1, 1, 2, 2]    [0, 0, 0, 0, 0]
# ['B', 'B', 'R', 'R', 'R']    [1, 1, 2, 2, 2]    [0, 0, 0, 0, 0]
# ['R', 'R', 'R', 'R', 'R']    [2, 2, 2, 2, 2]    [0, 0, 0, 0, 0]
