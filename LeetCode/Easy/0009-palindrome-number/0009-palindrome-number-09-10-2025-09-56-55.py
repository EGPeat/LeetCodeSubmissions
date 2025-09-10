class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x is None or x < 0:
            return False
        if x < 10:
            return True
        copynum = x
        high_modulator = 10
        low_modulator = 10
        while high_modulator <= x:
            high_modulator *= 10
        high_modulator /= 10
        
        while high_modulator >= low_modulator:
            high_num = copynum // high_modulator
            low_num = copynum % 10
            copynum %= high_modulator
            high_modulator /= 100
            copynum //= 10
            if high_num != low_num:
                return False
        return True