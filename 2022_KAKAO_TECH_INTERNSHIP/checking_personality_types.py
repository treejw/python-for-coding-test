# https://school.programmers.co.kr/learn/courses/30/lessons/118666

def solution(survey, choices):
    typeDict = {k:0 for k in 'RTCFJMAN'}
    
    for (a, b), choice in zip(survey, choices):
        score = choice - 4
        if score < 0:
            typeDict[a] -= score
        elif score > 0:
            typeDict[b] += score
    
    answer = ''
    for metric in ['RT','CF','JM','AN']:
        a, b = sorted([metric[0], metric[1]]) # 사전순
        answer += b if typeDict[a] < typeDict[b] else a
    return answer
