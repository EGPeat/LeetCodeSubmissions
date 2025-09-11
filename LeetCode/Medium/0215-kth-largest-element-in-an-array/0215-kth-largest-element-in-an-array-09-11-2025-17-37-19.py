class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        from heapq import heappop, heappush, heapify
        heap = []

        for num in nums:
            heappush(heap, -num)
        for num in range(k):
            if num == k-1:
                return -heappop(heap)
            heappop(heap)
        
        return 0 