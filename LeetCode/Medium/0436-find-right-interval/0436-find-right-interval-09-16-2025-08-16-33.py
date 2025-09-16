class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        n = len(intervals)
        result = [-1 for x in range(n)]
        starts = sorted((start, idx) for idx, (start, end) in enumerate(intervals))
      
        for idx, (_, end) in enumerate(intervals):
            spot = bisect_left(starts, (end, float('-inf')))
            if spot < n:
                result[idx] = starts[spot][1]
      
        return result