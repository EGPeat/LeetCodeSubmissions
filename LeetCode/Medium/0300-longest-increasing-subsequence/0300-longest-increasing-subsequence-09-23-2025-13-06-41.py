class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n1 = len(nums)
        dp = [1] * n1
        for i in range(1, n1):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)