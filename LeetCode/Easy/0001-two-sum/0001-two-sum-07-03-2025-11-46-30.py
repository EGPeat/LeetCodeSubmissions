class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
       for idx_one in range(len(nums)):
            for idx_two in range(idx_one + 1, len(nums)):
                if nums[idx_one] + nums[idx_two] == target:
                    return [idx_one, idx_two]

        