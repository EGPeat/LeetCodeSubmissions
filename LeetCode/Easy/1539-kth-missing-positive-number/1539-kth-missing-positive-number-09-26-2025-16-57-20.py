class Solution:
    def findKthPositive(self, nums: List[int], k: int) -> int:
        missingNumbers = []
        list_idx, n = 0, nums[-1]
        for search_idx in range(1, n):
            if len(missingNumbers) == k:
                return missingNumbers[-1]
            if nums[list_idx] == search_idx:
                list_idx += 1
            else:
                missingNumbers.append(search_idx)

        while len(missingNumbers) < k:
            n += 1
            missingNumbers.append(n)



        return missingNumbers[-1]
        #https://leetcode.com/problems/first-missing-positive/ can be helpful

