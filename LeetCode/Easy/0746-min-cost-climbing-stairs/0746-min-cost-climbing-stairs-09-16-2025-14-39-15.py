import math
class Solution:
    def minCostClimbingStairs(self, fee):
        n = len(fee)
        if not fee:
            return 0
        dp = [0 for _ in range(n)]
        dp[0] = fee[0]
        if n >= 2:
            dp[1] = fee[1]

        for i in range(2, n):
            dp[i] = fee[i] + min(dp[i-1], dp[i-2])
        print(fee, dp)
        return min(dp[-1], dp[-2])
