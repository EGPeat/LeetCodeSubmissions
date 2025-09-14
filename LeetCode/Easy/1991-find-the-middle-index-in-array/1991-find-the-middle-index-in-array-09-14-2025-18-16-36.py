class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        prefix_sum = [0] * len(nums)
        sum_nums = sum(nums)
        for idx in range(len(nums)):  # maybe need to cope with 0 and len(nums) - 1 values
            if idx != 0:
                prefix_sum[idx] = prefix_sum[idx - 1] + nums[idx - 1]
            if prefix_sum[idx] == sum_nums - prefix_sum[idx] - nums[idx]:
                return idx
        return -1
