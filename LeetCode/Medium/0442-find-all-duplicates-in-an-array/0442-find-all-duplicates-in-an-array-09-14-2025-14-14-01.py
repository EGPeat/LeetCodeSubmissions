class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        duplicateNumbers = []
        i, n = 0, len(nums)
        missingNumbers = []
        while i < n:
            j = nums[i] - 1
            if nums[i] != nums[j]:
                nums[i], nums[j] = nums[j], nums[i]
            else:
                i += 1
        for i in range(n):
            if nums[i] != (i + 1):
                duplicateNumbers.append(nums[i])

        return duplicateNumbers
