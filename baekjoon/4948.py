import sys
input = lambda: sys.stdin.readline().strip()

def prime_dp(limit=123456):
    n = limit*2
    is_prime = [1]*(n+1)
    is_prime[1] = 0

    for i in range(3, int(n**0.5)+1, 2):
        if is_prime[i]:
            for j in range(i*i, n+1, i*2):
                is_prime[j] = 0
    return is_prime

def solution(n, is_prime):
    if n == 1: return 1
    s = n+1 if n%2==1 else n
    return sum(is_prime[s+1:(2*n):2])

is_prime = prime_dp(123456)
while True:
    n = int(input())
    if n == 0:
        break
    print(solution(n, is_prime))
