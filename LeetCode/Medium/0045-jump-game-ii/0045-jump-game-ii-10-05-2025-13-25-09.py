
import math


class Solution:
    def jump(self, jumps):
        n = len(jumps)
        if n < 2:
            return 0
        count, loc = 0, 0
        jumper = [math.inf] * n
        jumper[0] = 0
        for loc in range(n):
            #print(jumper)
            for i in range(1, jumps[loc]+1):
                if loc + i < n:
                    #jumper[loc+i] += 1
                    jumper[loc+i] = min(jumper[loc+i], jumper[loc] + 1)
        #print(jumper)
        return jumper[-1]


    def canJump(self, nums: List[int]) -> bool:
        max_reachable = 0
        for current_pos, jump_length in enumerate(nums):
            if max_reachable < current_pos:
                return False
            max_reachable = max(max_reachable, current_pos + jump_length)
        return True