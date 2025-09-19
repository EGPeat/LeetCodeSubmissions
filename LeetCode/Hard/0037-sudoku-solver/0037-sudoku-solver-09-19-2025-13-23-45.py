class Solution:
    def validate(self, board, x, y, testing=None):
        #print(f"Main location is ({x},{y}) with value {board[x][y]}")
        if not testing:
            spot_val = board[x][y]
        else:
            spot_val = testing
        if spot_val == ".":
            return True
        for i, val in enumerate(board[x]):
            if val == spot_val and i != y:
                return False
        for val in range(0, 9):
            if board[val][y] == spot_val and val != x:
                return False
        for x2 in range(0, 3):
            for y2 in range(0, 3):
                new_x = (x//3)*3 + x2
                new_y = (y//3)*3 + y2
                if new_x == x and new_y == y:
                    pass
                elif board[new_x][new_y] == spot_val:
                    return False
        return True

    def solveSudoku(self, board: List[List[str]]) -> None:
        self.row_used = [[False] * 9 for _ in range(9)]
        self.col_used = [[False] * 9 for _ in range(9)]
        self.block_used = [[[False] * 9 for _ in range(3)] for _ in range(3)]
        for x in range(9):
            for y in range(9):
                if board[x][y] == ".":
                    pass
                else:
                    self.flip(x, y, int(board[x][y]), True)
        
        #for num in range(1,5):
        #    if self.validate2(0, 2, num):
        #        return
        self.solve(board)

    def flip(self, x, y, value, is_true):
        #print(value, type(value))
        #print( self.row_used[x][value-1], type(self.row_used[x][value-1]))
        self.row_used[x][value-1] = is_true
        self.col_used[y][value-1] = is_true
        self.block_used[int(x//3)][int(y//3)][value-1] = is_true
    
    def validate2(self, x, y, new_val):
        #print(x, y, new_val)
        #print(self.row_used[x][new_val-1], self.row_used[x])
        #print(self.col_used[y][new_val-1], self.col_used[y])
        #print(self.block_used[int(x//3)][int(y//3)][new_val-1], self.block_used[int(x//3)][int(y//3)])
        #print("########################")
        if self.row_used[x][new_val-1]:
            return False
        if self.col_used[y][new_val-1]:
            return False
        if self.block_used[int(x//3)][int(y//3)][new_val-1]:
            return False
        return True

    def solve(self, board):

        for x in range(9):
            for y in range(9):
                if board[x][y] == ".":
                    for num in range(1,10):
                        if self.validate2(x, y, num):
                            board[x][y] = str(num)
                            self.flip(x, y, int(board[x][y]), True)
                            if self.solve(board):
                                return True
                            else:
                                self.flip(x, y, int(board[x][y]), False)
                                board[x][y] = "."
                    

                    return False
        return True