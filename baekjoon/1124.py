def solution(A, B):
    is_prime = dict()
    def check_prime(n):
        if is_prime.get(n): return is_prime[n]
        if n <= 1: return 0
        for i in range(2, int(n**0.5)+1):
            if n%i == 0:
                is_prime[n] = 0
                return is_prime[n]
        is_prime[n] = 1
        return is_prime[n]
    
    prime_nums = [n for n in range(2, B+1) if check_prime(n)]
    def count_primeNum(n):
        if check_prime(n): return 0
        cnt = 0
        while n > 1:
            for i in prime_nums:
                if n % i == 0:
                    n //= i
                    cnt += 1
                    break
        return cnt
    return sum([check_prime(count_primeNum(n)) for n in range(A, B+1)])

A, B = map(int, input().split())
print(solution(A, B))
