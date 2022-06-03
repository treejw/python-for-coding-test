def solution(X):
    array = [64]
    sum_len = sum(array)

    while sum_len != X:
        n = array.pop()
        half = n//2
        array.append(half)
        sum_len -= half

        if sum_len < X:
            array.append(half)
            sum_len += half

    return len(array)

X = int(input())
print(solution(X))