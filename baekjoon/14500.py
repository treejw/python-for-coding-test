import sys
input = lambda: sys.stdin.readline().strip()

class Tetromino:
    def __init__(self):
        self.tetromino = {
            0: [[1, 1, 1, 1]],
            1: [[1,1],
                [1,1]],
            2: [[1,0],
                [1,0],
                [1,1]],
            3: [[0,1],
                [0,1],
                [1,1]],
            4: [[1,0],
                [1,1],
                [0,1]],
            5: [[0,1],
                [1,1],
                [1,0]],
            6: [[1,1,1],
                [0,1,0]]
        }
        self.valid_rotate = [1, 0, 3, 3, 1, 1, 3]
        self.idx = 0
        self.rotateN = 0
        
    def get_item(self):
        return self.tetromino[self.idx]

    def rotate(self):
        prevR, prevC = len(self.tetromino[self.idx]), len(self.tetromino[self.idx][0])
        rotated = [[0]*prevR for _ in range(prevC)]
        for r in range(prevR):
            for c in range(prevC):
                rotated[c][prevR-1-r] = self.tetromino[self.idx][r][c]
        self.tetromino[self.idx] = rotated

    def generator(self):
        self.idx = 0
        while self.idx <= 6:
            yield self.get_item()
            if self.rotateN < self.valid_rotate[self.idx]:
                self.rotateN += 1
                self.rotate()
            else:
                self.idx += 1
                self.rotateN = 0
                
def solution(n, m, board):
    maxi = 0
    tetromino = Tetromino()
    for item in tetromino.generator():
        len_r, len_c = len(item), len(item[0])
        for r in range(n-len_r+1):
            for c in range(m-len_c+1):
                cur = sum([item[i][j]*board[r+i][c+j] for i in range(len_r) for j in range(len_c)])
                maxi = max(cur, maxi)
    return maxi

n, m = map(int, input().split())
board = []
for _ in range(n):
    board.append(list(map(int, input().split())))
print(solution(n, m, board))
