# https://school.programmers.co.kr/learn/courses/30/lessons/118668

from collections import defaultdict
from math import inf

def solution(alp, cop, problems):
    max_alp = max(alp, max([p[0] for p in problems]))
    max_cop = max(cop, max([p[1] for p in problems]))
    problems += [[0,0,1,0,1], [0,0,0,1,1]]
    
    dp = defaultdict(lambda:defaultdict(lambda:inf)) # dp[alp][cop] : alp, cop에 도달하기까지의 최단 시간
    dp[alp][cop] = 0
    
    for a in range(alp, max_alp+1):
        for c in range(cop, max_cop+1):
            for alp_req, cop_req, alp_rwd, cop_rwd, cost in problems:
                if a >= alp_req and c >= cop_req:
                    new_a, new_c = min(a+alp_rwd, max_alp), min(c+cop_rwd, max_cop)
                    dp[new_a][new_c] = min(dp[new_a][new_c], dp[a][c]+cost)
    return dp[max_alp][max_cop]
