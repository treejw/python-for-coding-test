import sys
input = lambda: sys.stdin.readline().strip()

def solution(n, words):
    words.sort(key=len)
    rm_words = 0
    for i in range(len(words)):
        for j in range(i+1, len(words)):
            if words[j].startswith(words[i]):
                rm_words += 1
                break
    return n - rm_words

n = int(input())
words = [input() for _ in range(n)]
print(solution(n, words))
