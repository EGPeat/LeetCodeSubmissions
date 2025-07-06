class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        counter = 1
        for idx in range(1, len(nums)-1):
            if nums[idx] <= nums[idx-1]:
                for idx2 in range(idx, len(nums)):
                    if nums[idx2] > nums[idx-1]:
                        nums[idx] = nums[idx2]
                        counter +=1
                        break
                if nums[idx] <= nums[idx-1]:
                    break
            else:
                counter += 1
        return counter