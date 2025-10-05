from typing import List
from bisect import bisect_left

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left_index = bisect_left(nums, target)
        right_index = bisect_left(nums, target + 1)
      
        if left_index == right_index:
            return [-1, -1]
        else:
            return [left_index, right_index - 1]