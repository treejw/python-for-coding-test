# https://school.programmers.co.kr/learn/courses/30/lessons/12987

from collections import deque

def solution(A, B):
    if max(B) < min(A):
        return 0
    B.sort(reverse=True)
    A.sort(reverse=True)

    answer = 0
    while B:
        b = B.pop()
        if A[-1] < b:
            A.pop()
            answer += 1
    return answer
