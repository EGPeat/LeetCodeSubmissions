class Solution:
    def longestPalindromeSubseq(self, st: str) -> int:
        n = len(st)
        dp = [[0 for _ in range(n)] for _ in range(n)]

        for i in range(n):
            dp[i][i] = 1

        for startIndex in range(n - 1, -1, -1):
            for endIndex in range(startIndex + 1, n):
                if st[startIndex] == st[endIndex]:
                    dp[startIndex][endIndex] = 2 + dp[startIndex + 1][endIndex - 1]
                else:
                    dp[startIndex][endIndex] = max(
                        dp[startIndex + 1][endIndex], dp[startIndex][endIndex - 1]
                    )
        return dp[0][n - 1]