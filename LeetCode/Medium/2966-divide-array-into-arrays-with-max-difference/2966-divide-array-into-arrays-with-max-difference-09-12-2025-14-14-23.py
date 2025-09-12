class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        if len(nums) % 3 != 0:
            return []
        nums.sort()
        output_array = []
        for idx in range(0, len(nums), 3):
            temp_array = nums[idx:idx+3]
            if max(temp_array) - min(temp_array) > k:
                return []
            else:
                output_array.append(temp_array)
        return output_array
