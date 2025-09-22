class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        lookat = []
        for x in range(len(matrix)):
            for y in range(len(matrix[0])):
                if matrix[x][y] == 0:
                    lookat.append((x, y))
        
        for x, y in lookat:
            for x2 in range(len(matrix)):
                matrix[x2][y] = 0
            for y2 in range(len(matrix[0])):
                matrix[x][y2] = 0