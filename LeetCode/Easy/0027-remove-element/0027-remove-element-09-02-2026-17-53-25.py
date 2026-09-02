class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i=0
        j=len(nums)-1
        for i in range(len(nums)):
            for j in range(len(nums)-1,-1,-1):
                if nums[i] != val:
                    break
                if (nums[i] == val and nums[j] != val):
                    nums[i], nums[j] = nums[j], nums[i]
                    break
                if i==j:
                    return i
        return len(nums)