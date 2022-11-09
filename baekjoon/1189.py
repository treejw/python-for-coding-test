import sys
input = sys.stdin.readline

def solution(R, C, K, board):
    start, dest = (R-1, 0), (0, C-1)
    move = [(-1,0), (0,1), (1,0), (0,-1)]
    
    def dfs(r, c, dist, visited):
        if (r,c) == dest and dist==K:
            return 1
        elif dist >= K:
            return 0
            
        ans = 0
        for dx, dy in move:
            nr, nc = r+dx, c+dy
            if 0<=nr<R and 0<=nc<C and visited[nr][nc]==0 and board[nr][nc]=='.':
                visited[nr][nc] = 1
                ans += dfs(nr, nc, dist+1, visited)
                visited[nr][nc] = 0
        return ans

    visited = [[0]*C for _ in range(R)]
    r, c = start
    visited[r][c] = 1
    return dfs(r, c, 1, visited)

R, C, K = map(int, input().strip().split())
board = []
for _ in range(R):
    board.append(input().strip())
print(solution(R, C, K, board))
