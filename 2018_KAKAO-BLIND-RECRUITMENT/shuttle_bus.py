# https://school.programmers.co.kr/learn/courses/30/lessons/17678

from heapq import heappush, heappop
from collections import deque

def time2sec(string):
    m,s = string.split(':')
    return int(m)*60 + int(s)

def sec2time(sec):
    m,s = divmod(sec, 60)
    return f'{m:02d}:{s:02d}'

def solution(n, t, m, timetable):
    first = time2sec('09:00')
    bus = deque([[first+i*t, m] for i in range(n)])
    
    queue = []
    for t in timetable:
        heappush(queue, time2sec(t))
    
    prev_t = 0
    while bus:
        start_t, remain_m = bus.popleft()
        while remain_m>0 and queue:
            t = heappop(queue)
            if t <= start_t:
                remain_m -= 1
                prev_t = max(t, prev_t)
            else:
                heappush(queue, t)
                break
        
        if not bus:
            return sec2time(start_t) if remain_m>0 else sec2time(prev_t-1)
