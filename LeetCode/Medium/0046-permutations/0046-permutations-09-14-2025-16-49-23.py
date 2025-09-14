from collections import deque


class Solution:
    def findPermutationsHelper(self, nums, result, input_list, new_num):
        input_list.append(new_num)
        if len(input_list) == len(nums):
            result.append(input_list)
        for number in nums:
            if number not in input_list:
                self.findPermutationsHelper(nums, result, input_list.copy(), number)
        return

    def permute(self, nums):
        result = []
        for number in nums:
            self.findPermutationsHelper(nums, result, [], number)
        return result
