class Solution:
    def merge(self, intervals):
        mergedIntervals = []
        intervals = sorted(intervals, key=lambda interval: interval[0])
        while len(intervals) > 1:
            tmp1 = intervals[0]
            tmp2 = intervals[1]
            if tmp1[1] >= tmp2[0]:
                tmp1[1]= max(tmp2[1], tmp1[1])
                tmp1[0] = min(tmp2[0], tmp1[0])
                intervals.pop(1)
            else:
                mergedIntervals.append(tmp1)
                intervals.pop(0)
        mergedIntervals.append(intervals[0])
        return mergedIntervals
   