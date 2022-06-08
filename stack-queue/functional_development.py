# https://programmers.co.kr/learn/courses/30/lessons/42586
# 기능개발


from math import ceil
from collections import deque

def solution(progresses, speeds):
    needDays = deque([ceil((100-p)/s) for p, s in zip(progresses, speeds)])

    cur = needDays.popleft()
    numDeyploy = [1]
    while needDays:
        new = needDays.popleft()
        if cur >= new:
            numDeyploy[-1] += 1
        else:
            numDeyploy.append(1)
            cur = new
    return numDeyploy