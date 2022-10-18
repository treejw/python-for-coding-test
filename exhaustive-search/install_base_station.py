# https://school.programmers.co.kr/learn/courses/30/lessons/12979

def solution(n, stations, w):
    stations = stations[::-1]
    answer = 0
    i = 1
    while i <= n:
        if not stations or abs(stations[-1]-i) > w:
            stations.append(i+w)
            answer += 1
        i = stations[-1]+w+1
        stations.pop()
    return answer
