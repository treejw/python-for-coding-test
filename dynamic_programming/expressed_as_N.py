from collections import defaultdict

def calc(set_a, set_b):
    res = set()
    for a in set_a:
        for b in set_b:
            res |= {a+b, a-b, b-a, a*b}
            if b != 0: res.add(a//b)
            if a != 0: res.add(b//a)
    return res

def solution(N, number):
    dp = defaultdict(set)               # dp[i] : N을 i번 사용했을 때, 만들 수 있는 숫자들
    for i in range(1, 9):
        n = int(str(N)*i)               # ex) 55, 555, ...
        dp[i].add(n)
        
        for j in range(1, i//2+1):      # +,-,*,//
            dp[i] |= calc(dp[j], dp[i-j])
        
        if number in dp[i]:
            return i
    return -1
