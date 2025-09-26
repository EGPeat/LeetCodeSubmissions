class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        n = len(nums)
        if n  < 2:
            return True

        i = 1
        while i < n and nums[i - 1] <= nums[i]:
            i += 1
        if i == n:
            return True
        i = 1
        while i < n and nums[i - 1] >= nums[i]:
            i += 1
        if i == n:
            return True
        return False
