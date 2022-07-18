# https://school.programmers.co.kr/learn/courses/30/lessons/42583
# 다리를 지나는 트럭

from collections import deque

def solution(bridge_length, weight, truck_weights):
    wait = deque(truck_weights)             # 대기중인 트럭
    on_brdg = deque([0]*bridge_length)      # 다리 위 상태  (ex) bridge_length=4 → on_brdg=[0, 0, 0, 0]
    on_brdg_weight = 0                      # 현재 다리 위에 있는 트럭 무게 총 합
    
    t = 0
    while wait or (on_brdg_weight > 0):
        # 다리 위 - 맨 앞 제거
        x = on_brdg.popleft()                             
        on_brdg_weight -= x                      
        
        # 다리 위 - 맨 뒤 추가
        if wait and (on_brdg_weight + wait[0] <= weight): 
            new = wait.popleft()
            on_brdg.append(new)
            on_brdg_weight += new
        else:
            on_brdg.append(0)
            
        t += 1
        
    return t
