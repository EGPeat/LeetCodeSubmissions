class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        from heapq import heapify, heappop, heappush
        heap = []
        theset = set()
        for num in nums:
            #print(num, heap, theset)
            if len(heap) < 3 and num not in theset:
                theset.add(num)
                heappush(heap, num)
            elif num > heap[0] and num not in theset:
                tmp = heappop(heap)
                #print("tmp is", tmp)
                theset.remove(tmp)
                heappush(heap, num)
                theset.add(num)
        output = 0
        if len(heap) < 3:
            while heap:
                output = heappop(heap)
        else:
            output = heappop(heap)
        return output    