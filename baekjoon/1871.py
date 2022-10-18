def func(car_num):
    s1, s2 = car_num.split('-')
    s1 = list(map(lambda x: ord(x)-ord('A'), list(s1)))
    n1 = sum([x*(26**i) for x, i in zip(s1, [2,1,0])])
    n2 = int(s2)
    if abs(n1-n2) <= 100:
        return 'nice'
    return 'not nice'

T = int(input())
for _ in range(T):
    car_num = input()
    print(func(car_num))
