class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        loc_check = [-1] * (len(nums) + 1)
        for num in nums:
            loc_check[num] = num
        for idx, number in enumerate(loc_check):
            if number == -1:
                return idx