class Solution:
    def isUgly(self, n: int) -> bool:
        if n <= 0:
            return False
        elif n == 1:
            return True
        else:
            for divisor in [2,3,5]:
                while True:
                    n2, rem = divmod(n, divisor)
                    if rem != 0:
                        break
                    n = n2
            if n == 1:
                return True
            else:
                return False