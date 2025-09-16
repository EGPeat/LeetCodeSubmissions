class Solution:
    def firstUniqChar(self, s: str) -> int:
        count_idx = {}
        letter_count = {}
        for char in s:
            letter_count[char] = letter_count.get(char, 0) + 1
        print(letter_count)

        for idx in range(len(s)):
            if letter_count[s[idx]] == 1:
                return idx
        return -1