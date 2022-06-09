# https://programmers.co.kr/learn/courses/30/lessons/42627
# 디스크 컨트롤러


import heapq as hq

def solution(jobs):
    total_len = len(jobs)

    jobs.sort(key=lambda x: (x[0], x[1]), reverse=True)
    readyQ = [(0,jobs.pop())]  # [(priority, job), ]
    
    ans = 0
    curT = 0
    while readyQ:
        _, (insertT, processT) = hq.heappop(readyQ)
        if curT < insertT:
            curT = insertT + processT
        else:
            curT += processT
        ans += (curT - insertT) # (curT - insertT + processT)
        
        # insert tasks into readyQ (in order of processT)
        while jobs:
            insertT, processT = jobs[-1]
            if insertT <= curT:
                hq.heappush(readyQ, (processT, jobs.pop()))
            else:
                break
        
        if (not readyQ) and jobs:
            readyQ.append((0, jobs.pop()))
        
    return ans//total_len