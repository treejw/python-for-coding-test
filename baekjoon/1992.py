import sys
input = lambda: sys.stdin.readline().strip()

def solution(n, board):
    sumi = set(sum(board, []))
    if sumi == {'0'}:
        return '0'
    elif sumi == {'1'}:
        return '1'
    else:
        left_top = solution(n//2, [board[i][:n//2] for i in range(n//2)])
        left_btm = solution(n//2, [board[i][:n//2] for i in range(n//2, n)])
        right_top = solution(n//2, [board[i][n//2:] for i in range(n//2)])
        right_btm = solution(n//2, [board[i][n//2:] for i in range(n//2, n)])
        return f'({left_top}{right_top}{left_btm}{right_btm})'

n = int(input())
board = [list(input()) for _ in range(n)]
print(solution(n, board))
