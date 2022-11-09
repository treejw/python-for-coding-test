import sys
input = sys.stdin.readline
from collections import defaultdict

is_prime = defaultdict(bool)

def check_primeN(n):
    global is_prime
    
    if n in is_prime:
        return is_prime[n]

    for i in range(2, int(n**0.5)+1):
        if n%i==0:
            is_prime[n] = False
            return is_prime[n]
    is_prime[n] = True
    return is_prime[n]

def solution(n):
    for i in range(3, (n//2)+1, 2):
        if check_primeN(i) and check_primeN(n-i):
            return f'{n} = {i} + {n-i}'
    return "Goldbach's conjecture is wrong."

while True:
    n = int(input().strip())
    if n==0:
        break
    print(solution(n))
