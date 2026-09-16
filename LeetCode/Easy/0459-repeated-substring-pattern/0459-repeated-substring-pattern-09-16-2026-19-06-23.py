class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        for i in range(1, len(s)//2+1):
            if len(s)%i == 0:
                temp = s[:i]*(len(s)//i)
                if temp == s:
                    return True
        return False