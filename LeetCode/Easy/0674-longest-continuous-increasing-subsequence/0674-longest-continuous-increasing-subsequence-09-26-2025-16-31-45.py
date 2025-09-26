class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        if not nums:
            return 0
        prev_val = nums[0]
        best_len, length = 1, 1
        for num in nums:
            if num > prev_val:
                length += 1
                prev_val = num
                best_len = max(best_len, length)
            else:
                length = 1
                prev_val = num
        return best_len