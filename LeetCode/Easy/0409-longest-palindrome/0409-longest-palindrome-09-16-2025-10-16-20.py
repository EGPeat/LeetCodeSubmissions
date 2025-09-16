class Solution:
    def longestPalindrome(self, s: str) -> int:
        if not s:
            return 0
        length = 0
        freq = {}
        odd_total = 0
        has_odd = False
        for idx in range(len(s)):
            freq[s[idx]] = freq.get(s[idx], 0) + 1
        for key in freq.keys():
            if freq[key] % 2 == 0:
                length += freq[key]
            else:
                odd_total += freq[key] - 1
                has_odd = True

        #print(odd_total, freq)
        if has_odd:
            length = length + odd_total + 1

        return max(length, 1) 