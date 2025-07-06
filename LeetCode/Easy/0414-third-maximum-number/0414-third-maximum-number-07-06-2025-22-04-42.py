class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        set_of_numbers = set(nums)
        if len(set_of_numbers) < 3:
            return max(set_of_numbers)
        set_of_numbers.remove(max(set_of_numbers))
        set_of_numbers.remove(max(set_of_numbers))
        return max(set_of_numbers)