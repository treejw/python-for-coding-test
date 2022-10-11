from collections import deque

def func(queue, nums):
    ans = 0
    for n in nums:
        if queue[0] != n:
            i = queue.index(n)
            if i <= len(queue)//2:
                queue.rotate(-i)
                ans += i
            else:
                queue.rotate(len(queue)-i)
                ans += len(queue)-i
        queue.popleft()
    return ans

N, M = map(int, input().split())
nums = list(map(int, input().split()))
queue = deque(range(1, N+1))
print(func(queue, nums))
