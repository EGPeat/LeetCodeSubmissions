class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minnum = float('inf')
        maxnum = 0
        maxgain = 0
        for num in prices:
            if num > maxnum:
                maxnum = num
                maxgain = max(maxgain, maxnum - minnum)
            if num < minnum:
                minnum = num
                maxnum = num
        return maxgain