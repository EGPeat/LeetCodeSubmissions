class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        dp = [[0 for _ in range(len(grid[0]))] for _ in range(len(grid))]

        dp[0][0] = grid[0][0]
        for c in range(1, len(grid[0])):
            dp[0][c] = grid[0][c] + dp[0][c-1]

        for r in range(1, len(grid)):
            dp[r][0] = grid[r][0] + dp[r-1][0]

        for r in range(1, len(grid)):
            for c in range(1, len(grid[0])):
                
                dp[r][c] = min(grid[r][c] + dp[r - 1][c], grid[r][c] + dp[r][c - 1])
        return dp[-1][-1]