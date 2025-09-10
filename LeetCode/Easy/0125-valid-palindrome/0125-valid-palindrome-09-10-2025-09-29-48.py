from string import ascii_letters, digits
class Solution:
    def isPalindrome(self, s: str) -> bool:
        start, end = 0, len(s) - 1
        while start < end:
            while start < end and s[start] not in ascii_letters and s[start] not in digits:
                start += 1
            while start < end and s[end] not in ascii_letters and s[end] not in digits:
                end -= 1
            if s[start].lower() != s[end].lower():
                return False
            start += 1
            end -= 1
        return True


        