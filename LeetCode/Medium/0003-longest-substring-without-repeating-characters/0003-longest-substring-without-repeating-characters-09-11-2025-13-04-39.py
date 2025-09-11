class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        curr_dict = {}
        length = 0 #need to do end - len(check)
        start = 0
        for end in range(len(s)):
            curr_dict[s[end]] = curr_dict.get(s[end], 0) + 1
            while curr_dict[s[end]] >= 2:
                curr_dict[s[start]] = curr_dict.get(s[start], 0) - 1
                start += 1
            length = max(length, end - start + 1)
        return length