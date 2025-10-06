class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        amount_of_operations = 0
        nums.sort(reverse=True)
        maxed_numbers = 0
        i = 0
        while max(nums) != min(nums):
            max_val = max(nums)
            while i < len(nums) and nums[i] == max_val:
                nums[i] = 0
                maxed_numbers += 1
                i += 1
            amount_of_operations += maxed_numbers



        return amount_of_operations - maxed_numbers