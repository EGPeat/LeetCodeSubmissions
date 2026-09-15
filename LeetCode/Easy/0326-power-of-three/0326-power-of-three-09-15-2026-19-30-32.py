class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n == 1:
            return True
        if n < 3:
            return False
        while True:
            n, remainder = divmod(n, 3)
            if remainder != 0:
                return False
            if n == 1:
                return True