def solution(N, r, c, cnt=0):
    N //= 2
    if N == 1:
        if r < N and c < N:
            return 0
        elif r < N and c >= N:
            return 1
        elif r >= N and c < N:
            return 2
        elif r >= N and c >= N:
            return 3
    
    if r < N and c < N:
        cnt += solution(N, r, c)
    elif r < N and c >= N:
        cnt += (N*N)+solution(N, r, c-N)
    elif r >= N and c < N:
        cnt += 2*(N*N)+solution(N, r-N, c)
    elif r >= N and c >= N:
        cnt += 3*(N*N)+solution(N, r-N, c-N)
    return cnt

N, r, c = map(int, input().strip().split())
print(solution(2**N, r, c))