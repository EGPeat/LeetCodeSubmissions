class Solution:
    def pal_check(self, s, left, right):
        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True
    def validPalindrome(self, s: str) -> bool:
        start = 0
        end = len(s) - 1
        while start <= end:
            char = s[start]
            alt_char = s[end]
            #print(first_mistake, char, alt_char)
            if char != alt_char:
                return self.pal_check(s, start, end - 1) or self.pal_check(s, start + 1, end)
            start += 1
            end -= 1

        return True
