class Solution:
    def validate(self, board, x, y):
        #print(f"Main location is ({x},{y}) with value {board[x][y]}")
        spot_val = board[x][y]
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
                #print(f"New Location is ({new_x}, {new_y}) with value {board[new_x][new_y]}")

                if new_x == x and new_y == y:
                    pass
                elif board[new_x][new_y] == spot_val:
                    return False
        
        return True
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #print(board[0], "\n", board[0][0])
        for x in range(9):
            for y in range(9):
                truth = self.validate(board, x, y)
                #print("#######################")
                if not truth:
                    return False
        return True