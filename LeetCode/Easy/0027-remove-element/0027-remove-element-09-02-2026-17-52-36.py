class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i=0
        j=len(nums)-1
        for i in range(len(nums)):
            print(nums)
            for j in range(len(nums)-1,-1,-1): #len(nums)-i?
                print(i, j)
                if nums[i] != val:
                    break
                if (nums[i] == val and nums[j] != val):
                    nums[i], nums[j] = nums[j], nums[i]
                    break

                if i==j:
                    print(f"len is {len(nums)-i} and i is {i}")
                    return i
        return len(nums)