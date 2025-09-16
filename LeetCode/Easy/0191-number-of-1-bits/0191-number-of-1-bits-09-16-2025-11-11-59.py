class Solution:
    def hammingWeight(self, n: int) -> int:
        stack = 0
        while n >= 1:
            stack += (n%2)
            n //= 2
        return stack