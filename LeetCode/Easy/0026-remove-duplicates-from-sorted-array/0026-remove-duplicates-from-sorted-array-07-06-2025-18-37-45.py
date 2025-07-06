class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        left, right = 0, 1
        if len(nums) < 2:
            return len(nums)
        while True:
            if nums[right] == nums[left]:
                right += 1
            elif nums[right] > nums[left]:
                left += 1
                nums[left] = nums[right]
            if right == len(nums):
                return left + 1
