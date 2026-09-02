class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        i = 0
        j = len(nums)-1
        while i<=j: #or i<=j
            mid = (i+j)//2
            #print(target, i, j, mid, nums[mid], nums)
            if nums[mid] == target:
                return mid
            if nums[mid] > target:
                j = mid-1
            else:
                i = mid+1
        return i