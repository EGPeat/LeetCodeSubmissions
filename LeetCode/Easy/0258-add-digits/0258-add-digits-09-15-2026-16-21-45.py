class Solution:
    def addDigits(self, num: int) -> int:
        while num >= 10:
            temp = 0
            while num > 0:
                num, remainder = divmod(num, 10)
                temp += remainder
            num = temp
        return num