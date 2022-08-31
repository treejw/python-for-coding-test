# https://school.programmers.co.kr/learn/courses/30/lessons/42889

from collections import Counter

def solution(N, stages):
    stage_n_users = Counter(stages)

    fail_rate = dict()
    n_arrival = len(stages)
    for i in range(1,N+1):
        fail_rate[i] = (stage_n_users[i])/(n_arrival) if n_arrival > 0 else 0
        n_arrival -= stage_n_users[i]
    return [k for k, v in sorted(fail_rate.items(), key=lambda x: -x[1])]
