# https://programmers.co.kr/learn/courses/30/lessons/64065
# 튜플

def solution(s):
    lists = eval(s.replace('{','[').replace('}',']'))
    lists = sorted(lists, key=lambda x: len(x))
    
    num_set = set()
    ans = list()
    for l in lists:
        n = (set(l) - num_set).pop()
        ans.append(n)
        num_set.add(n)
    return ans
