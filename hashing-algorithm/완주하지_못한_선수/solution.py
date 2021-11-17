# participant = ["mislav", "stanko", "mislav", "ana"]
# completion = ["stanko", "ana", "mislav"]

def solution(participant, completion):
    count_dict = dict()
    for c in completion:
        if c in count_dict: count_dict[c] += 1
        else:               count_dict[c] = 1
    
    for p in participant:
        if p not in count_dict:     return p
        count_dict[p] -= 1
        if count_dict[p] == -1:     return p
