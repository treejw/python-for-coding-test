import sys
input = sys.stdin.readline

def dfs(alive_ids, mafia, guilty, arr, night=0, max_night=0):
    if len(alive_ids) == 1 or mafia not in alive_ids: return night
    if max_night==len(guilty)//2: return max_night
    if len(alive_ids) % 2 == 0:
        night += 1
        for i, u_id in enumerate(alive_ids):
            if u_id == mafia: continue
            max_night = max(max_night, dfs(alive_ids[:i] + alive_ids[i+1:], mafia, [g + arr[u_id][j] for j, g in enumerate(guilty)], arr, night, max_night))
    else:
        max_i = max(range(len(alive_ids)), key=lambda x: guilty[alive_ids[x]])
        max_night = max(max_night, dfs(alive_ids[:max_i] + alive_ids[max_i+1:], mafia, guilty, arr, night, max_night))
    return max_night
    
N = int(input().strip())
guilty = list(map(int, input().strip().split()))
arr = [list(map(int, input().strip().split())) for _ in range(N)]
mafia = int(input().strip())

print(dfs(list(range(N)), mafia, guilty, arr))