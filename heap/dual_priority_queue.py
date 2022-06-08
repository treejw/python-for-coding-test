# https://programmers.co.kr/learn/courses/30/lessons/42628
# 이중우선순위큐


import heapq as hq

def solution(operations):
    heap = []
    for op in operations:
        if op == 'D 1':         # delete maximum
            if not heap: continue
            heap.pop()
        elif op == 'D -1':      # delete minimum
            if not heap: continue
            hq.heappop(heap)
        else:                   # insert num
            num = int(op.replace('I ', ''))
            hq.heappush(heap, num)
    
    if not heap:
        return [0, 0]
    return [max(heap), hq.heappop(heap)]