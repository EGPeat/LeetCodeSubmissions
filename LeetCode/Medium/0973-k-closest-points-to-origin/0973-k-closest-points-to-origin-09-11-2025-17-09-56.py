class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        from heapq import heapify, heappop, heappush
        heap = []
        for p in points:
            heappush(heap, (p[0]*p[0] + p[1]*p[1]    ,p[0], p[1]))
        #print(heap)
        output = []
        for i in range(k):
            tmp = heappop(heap)
            output.append((tmp[1], tmp[2]))
        return output