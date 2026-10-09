class Solution:
    def findPoisonedDuration(self, timeSeries: list[int], duration: int) -> int:
        cnt = 0
        for i in range(len(timeSeries)):
            curr_time = timeSeries[i]
            if i<len(timeSeries)-1 and timeSeries[i+1] <= curr_time+duration:
                cnt+= (timeSeries[i+1]-curr_time)
            else:
                cnt+= duration

        return cnt