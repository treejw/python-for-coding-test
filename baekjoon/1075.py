def solution(N, F):
    N = N[:-2]
    F = int(F)
    for x in range(0, 100):
        if int(N+'{:02d}'.format(x)) % F ==0:
            return '{:02d}'.format(x)
N = input()
F = input()
print(solution(N, F))