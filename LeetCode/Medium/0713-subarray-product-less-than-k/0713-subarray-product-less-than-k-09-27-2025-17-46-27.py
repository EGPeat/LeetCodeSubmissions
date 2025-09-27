class Solution:
    def numSubarrayProductLessThanK(self, nums, target):
        if target <= 1:
            return 0

        product = 1
        start = 0
        totalCount = 0

        for end in range(len(nums)):
            product *= nums[end]

            while product >= target:
                product //= nums[start]
                start += 1

            totalCount += end - start + 1

        return totalCount
