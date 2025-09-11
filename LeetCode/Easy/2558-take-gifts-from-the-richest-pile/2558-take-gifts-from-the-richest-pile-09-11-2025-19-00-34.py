class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        import heapq
        import math
        gifts = [item * -1 for item in gifts]
        heapq.heapify(gifts)
        for i in range(k):
            #temp = heapq.heappop(gifts)
            #temp = -math.floor(math.sqrt(-temp))
            #heapq.heappush(gifts, temp)

            heapq.heappush(gifts, -math.floor(math.sqrt(-heapq.heappop(gifts))))

        return abs(sum(gifts))