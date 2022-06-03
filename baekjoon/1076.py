def solution(c1, c2, c3):
    colors = ['black', 'brown', 'red', 'orange', 'yellow', 'green', 'blue', 'violet', 'grey', 'white']
    colors = {c:str(i) for i, c in enumerate(colors)}  

    n1, n2, n3 = map(lambda x: colors[x], [c1, c2, c3])
    res = int(n1+n2)*(10**int(n3)) 
    return res 

c1 = input()
c2 = input()
c3 = input()
print(solution(c1, c2, c3))