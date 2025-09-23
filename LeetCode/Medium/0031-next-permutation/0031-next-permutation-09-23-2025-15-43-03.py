class Solution:
    def find_range(self, nums, n):
        for i in range(n, -1, -1):
            for j in range(i, n + 1):
                if nums[i] < nums[j]:
                    return i
    def make_smaller(self, nums, n, index1):
        while index1 < n:
            #print(nums[index1:])
            curr_best = index1 + 1
            #print(index1, len(nums))
            #print(curr_best)
            for i in range(index1, n+1):
                #print(nums[i])
                if nums[i] < nums[index1] and nums[i] <= nums[curr_best]:
                    curr_best = i
            #print(f"for nums {nums}, curr_best is {curr_best} aka nums[curr_best] = {nums[curr_best]}")
            if nums[curr_best] < nums[index1]:
                nums[index1], nums[curr_best] = nums[curr_best], nums[index1]
            index1 += 1
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        maxed = True
        n = len(nums) - 1
        for i in range(n):
            if nums[i] < nums[i+1]:
                maxed = False
        print(f"maxed is {maxed}")  #use this to make it make the smallest
        p2 = len(nums) - 1
        p1 = len(nums) - 2
        if not maxed: #deal with maxed later
            index1 = self.find_range(nums, n)
            curr_best = index1 + 1
            for i in range(index1, n+1):
                #print(nums[i])
                if nums[i] > nums[index1] and nums[i] <= nums[curr_best]:
                    curr_best = i
            #print(f"for nums {nums}, curr_best is {curr_best} aka nums[curr_best] = {nums[curr_best]}")
            nums[index1], nums[curr_best] = nums[curr_best], nums[index1]
            index1 += 1
            self.make_smaller(nums, n, index1)
        else:
            self.make_smaller(nums, n, 0)
