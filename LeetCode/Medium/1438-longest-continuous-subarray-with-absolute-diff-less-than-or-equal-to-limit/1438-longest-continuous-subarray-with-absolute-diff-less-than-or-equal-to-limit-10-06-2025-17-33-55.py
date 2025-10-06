from collections import defaultdict


class Solution:
    def longestSubarray(self, nums, limit):
        sorted_window = SortedList()
        print(sorted_window)
        max_length = 0
        left = 0
      
        for right, num in enumerate(nums):
            sorted_window.add(num)
          
            while sorted_window[-1] - sorted_window[0] > limit:
                sorted_window.remove(nums[left])
                left += 1
          
            max_length = max(max_length, right - left + 1)
      
        return max_length