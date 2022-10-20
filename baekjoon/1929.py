import sys
input = sys.stdin.readline

def is_prime(num):
    if num == 1: return False
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            return False
    return True

def func(m, n):
    for num in range(m, n+1):
        if is_prime(num):
            print(num)

m, n = map(int, input().strip().split())
func(m, n)
