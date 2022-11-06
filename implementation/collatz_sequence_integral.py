def func(n, arr=[]):
    arr.append(n)
    if n == 1:
        return arr
    else:
        x = n//2 if n%2==0 else n*3+1
        return func(x, arr)

def calc_area(arr, a,b):
    if a >= b:
        return -1
    area = 0
    for i in range(a, b-1):
        y1, y2 = sorted([arr[i], arr[i+1]])
        area += y1 + (y2-y1)/2
    return area
        
def solution(k, ranges):
    answer = []
    arr = func(k)
    for a, b in ranges:
        b += len(arr)
        answer.append(calc_area(arr, a,b))
    return answer
