# https://school.programmers.co.kr/learn/courses/30/lessons/118670

from collections import deque

class Matrix:
    def __init__(self, arr):
        self.n_rows, self.n_cols = len(arr), len(arr[0])
        self.len_border = self.n_rows*self.n_cols - (self.n_rows-2)*(self.n_cols-2)
        
        self.left, self.right, self.middles = deque(), deque(), deque()
        for i in range(self.n_rows):
            self.left.append(arr[i][0])
            self.right.append(arr[i][-1])
            self.middles.append(deque(arr[i][1:-1]))
        
    def operate(self, operation, n_op):
        if operation == 'ShiftRow':
            self.shiftRow(n_op)
        else:
            self.rotate(n_op)

    def shiftRow(self, n_op):
        n_op %= self.n_rows
        self.left.rotate(n_op)
        self.middles.rotate(n_op)
        self.right.rotate(n_op)
            
    def rotate(self, n_op):
        n_op %= self.len_border
        for _ in range(n_op):
            self.middles[0].appendleft(self.left.popleft())
            self.right.appendleft(self.middles[0].pop())
            self.middles[-1].append(self.right.pop())
            self.left.append(self.middles[-1].popleft())
    
    def result(self):
        return [[self.left.popleft()] + list(self.middles.popleft()) + [self.right.popleft()] for _ in range(self.n_rows)]
    
def solution(rc, operations):
    matrix = Matrix(rc)
    n_op = 1
    for i in range(1, len(operations)+1): 
        if i < len(operations) and operations[i-1] == operations[i]:
            n_op += 1
        else:
            matrix.operate(operations[i-1], n_op)
            n_op = 1
    return matrix.result()
