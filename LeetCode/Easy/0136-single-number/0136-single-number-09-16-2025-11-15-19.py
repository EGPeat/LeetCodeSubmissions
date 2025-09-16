class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        n = len(nums) + 1
        x1 = 1
        for i in range(2, max(nums) + 1):
            x1 = x1 ^ i

        x2 = nums[0]
        for i in range(1, n - 1):
            x2 = x2 ^ nums[i]
        return x2