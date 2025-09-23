class Solution:
    def myPow(self, x: float, n: int) -> float:
        def quick_power(base: float, exponent: int) -> float:
            result = 1.0
            while exponent > 0:
                if exponent & 1:
                    result *= base
                base *= base
                exponent >>= 1
          
            return result
        if n >= 0:
            return quick_power(x, n)
        else:
            return 1.0 / quick_power(x, -n)