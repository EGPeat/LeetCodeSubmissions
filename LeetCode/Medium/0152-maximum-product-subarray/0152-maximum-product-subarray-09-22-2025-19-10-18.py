class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if not nums:
            return 0

        maxCurrent = minCurrent = maxProduct = nums[0]

        for i in range(1, len(nums)):
            if nums[i] < 0:
                maxCurrent, minCurrent = minCurrent, maxCurrent
            maxCurrent = max(nums[i], maxCurrent * nums[i])
            minCurrent = min(nums[i], minCurrent * nums[i])
            maxProduct = max(maxProduct, maxCurrent)

        return maxProduct