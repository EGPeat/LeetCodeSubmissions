class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        s = sum(nums)
        n = len(nums)  #nums
        if s % 2 == 1:
            return False
        capacity = s//2

        
        if capacity <= 0 or n == 0:
            return 0

        dp = [[False for x in range(capacity + 1)] for y in range(n + 1)]

        dp[0][0] = True

        for i in range(1, n+1):
            current_num = nums[i - 1]
            for j in range(1, capacity + 1):
                dp[i][j] = dp[i - 1][j]
                if j >= current_num:
                    dp[i][j] = dp[i][j] or dp[i - 1][j - current_num]
        return dp[n][capacity]

