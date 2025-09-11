class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        result = [0] * len(nums)  
        for idx in range(len(nums)):
            if idx > 0:
                result[idx] = result[idx - 1] + nums[idx]
            else:
                result[idx] = nums[idx]
        return result