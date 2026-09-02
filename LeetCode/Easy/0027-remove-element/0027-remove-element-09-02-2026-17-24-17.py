class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i=0
        j=len(nums)-1
        count=0
        while i<=j:
            while j>=0 and nums[j]==val:
                count+=1
                j-=1
            print(count, i, j, nums)
            if j>=0 and nums[i]==val and i<=j:
                nums[i], nums[j] = nums[j], nums[i]
                j-=1
                count+=1
            i+=1
        print(count, i, j, nums)
        return len(nums)-count