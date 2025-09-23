class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        le, r = 0, len(matrix) - 1

        while le <= r:
            m = le + (r-le)//2
            if m == len(matrix) - 1 and matrix[m][0] <= target:
                break
            elif matrix[m][0] <= target and matrix[m+1][0] > target:
                break
            elif matrix[m][0] < target:
                le = m + 1
            elif matrix[m][0] > target:
                r = m - 1
        row = m
        le, r = 0, len(matrix[m]) - 1
        print(row, le, r, le + (r-1)//2)
        while le <= r:
            m = le + (r-le)//2
            if matrix[row][m] == target:
                return True
            elif matrix[row][m] > target:
                r = m - 1
            elif matrix[row][m] < target:
                le = m + 1
        return False