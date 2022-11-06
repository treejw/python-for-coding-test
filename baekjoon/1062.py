from itertools import combinations
import sys
input = sys.stdin.readline

def word2bit(bit_dict, w_set):
    bit_word = 0
    for c in w_set:
        bit_word |= (1 << bit_dict[c])
    return bit_word

def solution(k, words):
    lang = set('antatica')
    if k < len(lang):
        return 0
    
    k -= len(lang)
    used = set()
    wBook = []
    cnt = 0
    for word in words:
        if len(word) == 8: cnt += 1    # antatica
        else:
            word = set(word[4:-4]) - lang
            if len(word) > k:
                continue
            wBook.append(word)
            used |= word
    
    if len(used) <= k:
        return cnt + len(wBook)

    bit_dict = {c:i for i, c in enumerate(used)}
    wBook = [word2bit(bit_dict, w_set) for w_set in wBook]
    
    maxi = cnt
    for case in combinations(used, k):
        cur = cnt
        case_bit = word2bit(bit_dict, case)
        for w_bit in wBook:
            if w_bit == w_bit & case_bit:
                cur += 1
        maxi = max(cur, maxi)
    return maxi

n, k = map(int, input().strip().split())
words = [input().strip() for _ in range(n)]
print(solution(k, words))
