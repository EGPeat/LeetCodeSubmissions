from functools import cache
from bisect import bisect_left
from typing import List
class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        jobs = sorted(zip(startTime, endTime, profit))
        n = len(jobs)
        @cache
        def dfs(index: int) -> int:
            if index >= n:
                return 0
            current_start, current_end, current_profit = jobs[index]
            next_valid_job_index = bisect_left(
                jobs, 
                current_end, 
                lo=index + 1, 
                key=lambda job: job[0]
            )
          
            skip_current = dfs(index + 1)
            take_current = current_profit + dfs(next_valid_job_index)
          
            return max(skip_current, take_current)
        return dfs(0)