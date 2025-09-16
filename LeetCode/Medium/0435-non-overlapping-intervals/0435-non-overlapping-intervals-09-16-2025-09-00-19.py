class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        replace = 0
        starts = sorted((start, end, idx) for idx, (start, end) in enumerate(intervals))
        #intervals = sorted(intervals, key=lambda interval: interval[1])
        print(starts)
        output = [False] * len(intervals)
        previous = starts.pop(0)
        counter = 0
        
        for inter in starts:
            #print(previous, inter, output, counter, replace)
            if previous[1] > inter[0]:
                output[inter[2]] = True
                counter += 1
            else:
                #if counter > 0:
                #    replace += counter - 1
                replace += counter
                counter = 0
                output[inter[2]] = False
                previous = inter
        #print(output, counter, replace)
        return replace + counter