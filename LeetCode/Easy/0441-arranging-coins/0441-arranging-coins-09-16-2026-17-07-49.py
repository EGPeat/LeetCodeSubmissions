class Solution:
    def arrangeCoins(self, n: int) -> int:
        i = 1
        v = 1
        while v < n:
            i += 1
            v += i
        return i if v == n else i-1