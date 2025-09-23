class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        m, n = len(matrix), len(matrix[0])
        dp = [[0 for _ in range(n+1)] for _ in range(m+1)]
        max_val = 0

        for i in range(m):
            for j in range(n):
                print(f"i is {i}, j is {j}, matrix is {matrix[i][j]}")
                if matrix[i][j] == '0':
                    dp[i+1][j+1] = 0
                elif matrix[i][j] == '1':
                    tmp = min(dp[i][j+1], dp[i+1][j])
                    dp[i+1][j+1] = min(dp[i][j], tmp) + 1
                max_val = max(max_val, dp[i+1][j+1])

        return max_val * max_val