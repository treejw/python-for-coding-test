import sys
sys.setrecursionlimit(10**5)

def solution(M, N, arr, visited, coords):
    move = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    def dfs(x, y, visited, coords):
        visited[y][x] = 1
        for nx, ny in [(x + dx, y + dy) for dx, dy in move if (0<=x+dx<M) and (0<=y+dy<N)]:
            if visited[ny][nx]:
                continue
            visited[ny][nx] = 1
            if arr[ny][nx] == 1:
                coords.remove((nx, ny))
                visited, coords = dfs(nx, ny, visited, coords)
        return visited, coords

    cnt = 0
    while coords:
        x, y = coords.pop()
        visited, coords = dfs(x, y, visited, coords)
        cnt += 1
    return cnt


T = int(input())
for _ in range(T):
    M, N, K = map(int, input().split())
    arr = [[0]*M for _ in range(N)]
    visited = [[0]*M for _ in range(N)]
    coords = set()
    for _ in range(K):
        x, y = map(int, input().split())
        arr[y][x] = 1
        coords.add((x, y))
    print(solution(M, N, arr, visited, coords))
