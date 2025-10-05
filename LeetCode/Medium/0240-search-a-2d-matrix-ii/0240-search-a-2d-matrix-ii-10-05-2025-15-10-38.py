class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for row in matrix:
            position = bisect_left(row, target)
            if position < len(row) and row[position] == target:
                return True
        return False