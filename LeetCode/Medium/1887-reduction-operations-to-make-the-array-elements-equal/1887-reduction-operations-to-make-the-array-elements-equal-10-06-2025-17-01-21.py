class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        amount_of_operations = 0
        n = len(nums)
        nums.sort(reverse=True)
        maxed_numbers = 0
        i = 0
        if nums[0] == nums[-1]:
            return 0
        while i < n:
            max_val = nums[i]
            while i < n and nums[i] == max_val:
                #nums[i] = 0
                maxed_numbers += 1
                i += 1
            amount_of_operations += maxed_numbers



        return amount_of_operations - maxed_numbers