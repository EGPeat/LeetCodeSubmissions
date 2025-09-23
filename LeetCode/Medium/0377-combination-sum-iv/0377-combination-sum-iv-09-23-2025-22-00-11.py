class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        n = len(nums)
        if target <= 0 or n == 0:
              return 0
        dp = [0 for _ in range(target+1)]
        for num in nums:
            if num <= target:
                dp[num] = 1

        for i in range(target+1):
            for num in nums:
                if i + num <= target:
                    dp[i+num] += (dp[i])

        #print(dp)
        return dp[-1]