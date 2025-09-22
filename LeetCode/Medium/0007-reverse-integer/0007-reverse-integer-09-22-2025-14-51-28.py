class Solution:
    def reverse(self, x: int) -> int:
        output = 0
        isneg = False
        if x < 0:
            isneg = True
            x *= -1
        while x > 0:
            output *= 10
            output += x%10
            x //= 10
        if isneg:
            output *= -1
        if output > (pow(2, 31) - 1) or output < -pow(2,31):
            output = 0
        return output