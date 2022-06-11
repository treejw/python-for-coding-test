# https://programmers.co.kr/learn/courses/30/lessons/12952
# N-Queen


def is_possible(r_i, rows):
    for i in range(r_i):
        if rows[i]==rows[r_i]: # same column
            return False
        elif abs(rows[i]-rows[r_i]) == abs(i-r_i): # same diagonal
            return False
    return True

def dfs(r_i, n, rows, ans=0):
    if r_i == n:
        return 1
    ans = 0
    for c in range(n):
        rows[r_i] = c
        if is_possible(r_i, rows):
            ans += dfs(r_i+1, n, rows)
    return ans

def solution(n):
    # 각 row에서 queen이 있는 column index
    rows = [0 for _ in range(n)]
    return dfs(0, n, rows)
