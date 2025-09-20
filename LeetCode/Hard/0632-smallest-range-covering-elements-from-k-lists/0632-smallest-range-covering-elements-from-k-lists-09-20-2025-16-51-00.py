from typing import List
from collections import Counter
from math import inf

class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        elements = [(value, list_index) for list_index, list_values in enumerate(nums) for value in list_values]
        elements.sort()
        list_counter = Counter()
        min_range = [-inf, inf]
        left = 0
        for right, (right_value, list_index) in enumerate(elements):
            list_counter[list_index] += 1
            while len(list_counter) == len(nums):
                left_value = elements[left][0]
                current_range_diff = right_value - left_value - (min_range[1] - min_range[0])

                if current_range_diff < 0 or (current_range_diff == 0 and left_value < min_range[0]):
                    min_range = [left_value, right_value]

                list_counter[elements[left][1]] -= 1
                if list_counter[elements[left][1]] == 0:
                    list_counter.pop(elements[left][1])
                left += 1
      
        return min_range
