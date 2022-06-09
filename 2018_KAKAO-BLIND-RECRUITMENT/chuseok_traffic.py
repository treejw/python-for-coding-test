# https://programmers.co.kr/learn/courses/30/lessons/17676
# [1차] 추석 트래픽


from collections import defaultdict

def time2msecs(S):
    h,m,s = map(float, S.split(':'))
    return int(h*60*60*1000 + m*60*1000 + s*1000)

def solution(lines):
    logDict = defaultdict(int)
    for logId, log in enumerate(lines):
        _, S, T = log.split()
        S_end = time2msecs(S) + 3000
        S_start = S_end - int(float(T[:-1])*1000) + 1
        logDict[S_start] += 1
        logDict[S_end+1000] -= 1
    
    cur_Nreq = max_Nreq = 0
    for t in sorted(logDict):
        cur_Nreq += logDict[t]
        max_Nreq = max(cur_Nreq, max_Nreq)
    return max_Nreq
