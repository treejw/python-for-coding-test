from collections import defaultdict
import sys
input = lambda: sys.stdin.readline().strip()
    
def solution(n):
    if n < 10:
        return n
    elif n > 1022: # 1022 => 9876543210
        return -1

    def mk_dp(n):
        dp = defaultdict(dict)    # dp[i][j]: i자리수 숫자이면서, j으로 시작하는 수의 개수
        cnt = -1
        for i in range(1, 11):    # max_len = 10(9876543210)
            for j in range(10):
                if i == 1:
                    dp[i][j] = 1
                else:
                    dp[i][j] = sum([dp[i-1][k] for k in range(j)])
                if cnt+dp[i][j] >= n:
                    return dp, cnt, i, j
                cnt += dp[i][j]

    def func(len_n, last_num, cnt, num): 
        num = str(last_num)
        if len_n == 0:
            return num
        elif cnt == n:
            while len(num) <= len_n:
                num += str(int(num[-1])-1)
            return num
        for k in range(last_num):
            cnt += dp[len_n][k]
            if cnt >= n:
                if cnt > n:
                    cnt -= dp[len_n][k]
                num += func(len_n-1, k, cnt, num)
                break
        return num
            
    dp, cnt, len_num, last_num = mk_dp(n)
    return func(len_num-1, last_num, cnt, '')
    
n = int(input())
print(solution(n))

# len_num=1
# 0~9 : 10

# len_num=2
# 10 : 1
# 21, 20: 2
# 32, 31, 30: 3
# 99, 98, .., 91, 90: 10

# len_num=3
# 100: x
# 210: 1
# 321 320 310: 2+1=3
# 432 431 430 421 420 410: 3+2+1=6

# len_num=4
# 1000, 2000: x
# 3210: 1
# 4321 4320 4310 4210: 3+2+1
# 5432 5431 5430 5421 5420 5410 5321 5320 5310 5210: 6+3+1
