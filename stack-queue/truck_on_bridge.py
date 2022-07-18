# https://school.programmers.co.kr/learn/courses/30/lessons/42583
# 다리를 지나는 트럭

from collections import deque

def solution(bridge_length, weight, truck_weights):
    wait = deque(truck_weights)             
    on_brdg = deque([0]*bridge_length)   
    on_brdg_weight = 0
    
    t = 0 
    while wait or on_brdg_w > 0:
        x = on_brdg.popleft()                             
        on_brdg_weight -= x                      
        
        if wait and (on_brdg_weight + wait[0] <= weight): 
            new = wait.popleft()
            on_brdg.append(new)
            on_brdg_weight += new
        else:
            on_brdg.append(0)
            
        t += 1
        
    return t
