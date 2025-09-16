class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        if len(s) == 1:
            return ""
        count = {char: s.count(char) for char in set(s)}
        bad = set()
        for char in ascii_lowercase:
            if char in count.keys() and char.upper() not in count.keys():
                bad.add(char)
            elif char not in count.keys() and char.upper() in count.keys():
                bad.add(char.upper())

        if not bad:
            return s
        for char in bad:
            index = s.find(char)

            first = self.longestNiceSubstring(s[0:index])
            second = self.longestNiceSubstring(s[index+1:])
            print(first, second)
            if len(first) > len(second) or len(first) == len(second):
                return first
            else:
                return second