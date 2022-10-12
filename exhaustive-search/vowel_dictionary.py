# https://school.programmers.co.kr/learn/courses/30/lessons/84512

import sys
sys.setrecursionlimit(6**5)

def solution(word):
    vowels = ['A', 'E', 'I', 'O', 'U']

    def recursion(cur, dest, i=1):
        if cur == dest:
            return i
        v_idx = 0
        if len(cur)==5:
            v = cur.pop()
            while v == 'U':
                v = cur.pop()
            v_idx = vowels.index(v)+1
        cur.append(vowels[v_idx])
        return recursion(cur, dest, i+1)
    
    return recursion(cur=['A'], dest=list(word))
