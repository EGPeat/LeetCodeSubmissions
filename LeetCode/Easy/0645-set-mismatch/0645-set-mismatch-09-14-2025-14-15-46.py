class Solution:
    def findErrorNums(self, nums):
        i, n = 0, len(nums)
        while i < n:
            j = nums[i] - 1
            if nums[i] != nums[j]:
                nums[i], nums[j] = nums[j], nums[i]  # swap
            else:
                i += 1

        # find the first number missing from its index, that will be our required number
        for i in range(n):
            if nums[i] != (i + 1):
                # return [i+1,nums[i+1]]
                return [nums[i], i + 1]

        return [-1, -1]
