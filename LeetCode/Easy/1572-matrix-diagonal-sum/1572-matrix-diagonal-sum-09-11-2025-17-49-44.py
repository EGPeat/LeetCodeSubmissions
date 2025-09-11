class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        total_sum = 0
        left, right = 0, len(mat)-1
        for idx in range(len(mat)):
            if left != right:
                total_sum += mat[idx][left]
                total_sum += mat[idx][right]
            else:
                total_sum += mat[idx][left]
            left += 1
            right -= 1
        return total_sum