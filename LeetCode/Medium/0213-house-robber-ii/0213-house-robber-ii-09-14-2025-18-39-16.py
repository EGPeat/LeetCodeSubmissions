class Solution:
    def rob(self, wealth):
        n = len(wealth)
        if n == 1 or n == 2:
            return max(wealth)
        dp = [-math.inf for _ in range(n)]
        dp2 = [-math.inf for _ in range(n)]
        dp[0] = wealth[0]
        dp[1] = wealth[1]
        dp2[-1] = wealth[-1]
        dp2[-2] = wealth[-2]

        for start in range(0, n-1):
            end = start + 2
            while end < n-1:
                dp[end] = max(dp[end], dp[start] + wealth[end])
                end += 1
        
        for start in range(n - 1, 0, -1):
            end = start - 2
            while end > 0:
                dp2[end] = max(dp2[end], dp2[start] + wealth[end])
                end -= 1

        return max(max(dp), max(dp2))
