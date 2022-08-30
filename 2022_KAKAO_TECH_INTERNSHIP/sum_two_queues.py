# https://school.programmers.co.kr/learn/courses/30/lessons/118667

def solution(queue1, queue2):
    sum1, sum2 = sum(queue1), sum(queue2)
    queue_all = queue1 + queue2
    
    idx1_start, idx1_end = 0, len(queue1)-1
    idx2_start, idx2_end = len(queue1), len(queue_all)-1
    
    answer = 0
    while answer < 2 * len(queue_all):
        if sum1 == sum2:
            return answer
        
        if sum1 > sum2:
            x = queue_all[idx1_start]
            sum1, sum2 = sum1-x, sum2+x
            idx2_end = idx2_end+1 if idx2_end < len(queue_all)-1 else 0
            idx1_start = idx1_start+1 if idx1_start < len(queue_all)-1 else 0
            
        elif sum1 < sum2:
            x = queue_all[idx2_start]
            sum1, sum2 = sum1+x, sum2-x
            idx1_end = idx1_end+1 if idx1_end < len(queue_all)-1 else 0
            idx2_start = idx2_start+1 if idx2_start < len(queue_all)-1 else 0
            
        answer += 1
    
    return -1
