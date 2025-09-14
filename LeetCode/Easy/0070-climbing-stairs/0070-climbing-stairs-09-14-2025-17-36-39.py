class Solution:
    def climbStairs(self, n):
        if n == 0:
            return 1
        starter = [0 for y in range(n + 1)]
        starter[0] = 1
        for i in range(n + 1):
            if (i + 1) < n + 1:
                starter[i + 1] += starter[i]
            if (i + 2) < n + 1:
                starter[i + 2] += starter[i]
        return starter[-1]
