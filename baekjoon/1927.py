from heapq import heappush, heappop
import sys
input = sys.stdin.readline

n = int(input().strip())
heap = []
for _ in range(n):
    x = int(input().strip())
    if x == 0:
        print(heappop(heap) if heap else 0)
    else:
        heappush(heap, x)
