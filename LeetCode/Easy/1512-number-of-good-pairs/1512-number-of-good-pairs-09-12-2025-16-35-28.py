class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        pairCount = 0
        hashmap = {}
        for num in nums:
            if num in hashmap.keys():
                pairCount += hashmap[num]
                hashmap[num] += 1
            else:
                hashmap[num] = 1
        return pairCount