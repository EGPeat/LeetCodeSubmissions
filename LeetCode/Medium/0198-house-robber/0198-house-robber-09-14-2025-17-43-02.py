class Solution:
    def rob(self, wealth):
        n = len(wealth)
        if n == 1 or n == 2:
            return max(wealth)
        dp = [-math.inf for _ in range(n)]
        dp[0] = wealth[0]
        dp[1] = wealth[1]

        for start in range(0, n):
            end = start + 2
            while end < n:
                dp[end] = max(dp[end], dp[start] + wealth[end])
                end += 1
        return max(dp)