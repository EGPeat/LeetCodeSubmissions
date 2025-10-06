
from heapq import *


class Solution:
    def findLeastNumOfUniqueInts(self, nums, k):
        num_dict = {}
        for item in nums:
            num_dict[item] = num_dict.get(item, 0) + 1
        heap = []
        for key, value in num_dict.items():
            heappush(heap, (value, key))
        #print(heap)
        while k and heap:
            #print(k, heap)
            tmp = heappop(heap)
            if tmp[0] <= k:
                k -= tmp[0]
            else:
                heappush(heap, (tmp[0] - k, tmp[1]))
                k = 0
        #print(heap)
        return len(heap)