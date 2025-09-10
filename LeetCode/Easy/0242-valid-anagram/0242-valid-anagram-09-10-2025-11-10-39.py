class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        from collections import defaultdict
        if len(s) != len(t):
            return False
        char_count = defaultdict(int)
        for c in s:
            char_count[c] += 1
      
        for char in t:
            char_count[char] -= 1
            if char_count[char] < 0:
                return False
        return True
        