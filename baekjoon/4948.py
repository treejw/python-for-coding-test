from collections import defaultdict
import sys
input = lambda: sys.stdin.readline().strip()

def prime_dp(num):
    is_prime = defaultdict(lambda: True)
    is_prime[1] = False
    n = num*2
    for i in range(2, int(n**0.5)+1):
        if is_prime[i]:
            for j in range(i*i, n+1, i):
                is_prime[j] = False
    return is_prime

def solution(n, is_prime):
    if n == 1: return 1
    ans = 0
    s = n+1 if n%2==1 else n
    for num in range(s+1, 2*n, 2):
        if (num not in is_prime) or is_prime[num]:
            ans += 1
    return ans

is_prime = prime_dp(123456)
while True:
    n = int(input())
    if n == 0:
        break
    print(solution(n, is_prime))
