import sys
input = lambda: sys.stdin.readline().strip()
    
n = int(input())
emps = set()
for _ in range(n):
    name, flag = input().split()
    if flag=='enter':
        emps.add(name)
    elif name in emps:
        emps.remove(name)
print(*sorted(emps, reverse=True), sep='\n')
