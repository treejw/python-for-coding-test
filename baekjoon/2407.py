from math import factorial

def comb(n, m):
    return factorial(n) // (factorial(m)*factorial(n-m))

n, m = map(int, input().split())
print(comb(n, m))
