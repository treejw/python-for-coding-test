# https://programmers.co.kr/learn/courses/30/lessons/42626
# 더 맵게


import heapq

def solution(scoville, K):
    heapq.heapify(scoville)
    
    cnt = 0
    
    while scoville:
        cur = heapq.heappop(scoville)
        if cur >= K: 
            return cnt
        if scoville:
            new = heapq.heappop(scoville)
            update = cur + new*2
            heapq.heappush(scoville, update)
            cnt += 1
    return -1