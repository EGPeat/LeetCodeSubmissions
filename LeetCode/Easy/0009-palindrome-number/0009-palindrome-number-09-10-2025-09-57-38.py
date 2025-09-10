class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x is None or x < 0:
            return False
        if x < 10:
            return True
        high_modulator = 10
        low_modulator = 10
        while high_modulator <= x:
            high_modulator *= 10
        high_modulator /= 10
        
        while high_modulator >= low_modulator:
            high_num = x // high_modulator
            low_num = x % 10
            x %= high_modulator
            high_modulator /= 100
            x //= 10
            if high_num != low_num:
                return False
        return True