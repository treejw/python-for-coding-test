# https://programmers.co.kr/learn/courses/30/lessons/17677
# [1차] 뉴스 클러스터링


from collections import Counter

def solution(str1, str2):
    str1Dict = Counter([str1[i:i+2].lower() if str1[i:i+2].isalpha() else '' for i in range(0,len(str1)-1)])
    str2Dict = Counter([str2[i:i+2].lower() if str2[i:i+2].isalpha() else '' for i in range(0,len(str2)-1)])

    if '' in str1Dict: del str1Dict['']
    if '' in str2Dict: del str2Dict['']
    
    n1 = sum((str1Dict & str2Dict).values())
    n2 = sum((str1Dict | str2Dict).values())
    
    answer = n1/n2 if n2 > 0 else 1
    return int(answer * 65536)