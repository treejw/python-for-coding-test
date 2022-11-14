import sys
input = lambda: sys.stdin.readline().strip()
from collections import defaultdict

def solution(n):
    if n == 1:
        return 0, [1]
        
    dp = defaultdict(lambda: 1e6)

    def dfs(num, route, best_route):
        if num == 1:
            return route
        elif best_route and len(route) >= len(best_route):
            return best_route
            
        if num > 2 and num % 3 == 0 and dp[num//3] > len(route)+1:
            dp[num//3] = len(route)+1
            new_route = dfs(num//3, route+[num//3], best_route)
            best_route = min([new_route, best_route], key=len) if best_route else new_route
        if num > 1 and num % 2 == 0 and dp[num//2] > len(route)+1:
            dp[num//2] = len(route)+1
            new_route = dfs(num//2, route+[num//2], best_route)
            best_route = min([new_route, best_route], key=len) if best_route else new_route
        if num > 1 and dp[num-1] > len(route)+1:
            dp[num-1] = len(route)+1
            new_route = dfs(num-1, route+[num-1], best_route)
            best_route = min([new_route, best_route], key=len) if best_route else new_route
        return best_route
        
    route = dfs(n, [n], [])
    return len(route)-1, route
        
n = int(input())
ans, route = solution(n)
print(ans)
print(*route)
