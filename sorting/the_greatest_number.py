# https://programmers.co.kr/learn/courses/30/lessons/42746
# 가장 큰 수


def quicksort(nums):
    if len(nums) <= 1:
        return nums
    
    pivot = nums[len(nums)//2]
    left, equal, right = [], [], []
    
    for n in nums:
        if n+pivot > pivot+n:
            left.append(n)
        elif n+pivot == pivot+n:
            equal.append(n)
        else:
            right.append(n)
    return quicksort(left) + equal + quicksort(right)
    

def solution(numbers):
    if set(numbers) == {0}:
        return '0'
    
    nums = quicksort(list(map(str, numbers)))
    return ''.join(nums)
