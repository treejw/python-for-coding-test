from collections import deque
import sys
input = sys.stdin.readline

N = int(input().strip())
queue = deque()
for _ in range(N):
    cmd = input().strip().split()
    if cmd[0] == 'push':
        queue.append(int(cmd[1]))
    elif cmd[0] == 'pop':
        x = queue.popleft() if queue else -1
        print(x)
    elif cmd[0] == 'size':
        print(len(queue))
    elif cmd[0] == 'empty':
        print(1 if not queue else 0)
    elif cmd[0] == 'front':
        x = queue[0] if queue else -1
        print(x)
    elif cmd[0] == 'back':
        x = queue[-1] if queue else -1
        print(x)
