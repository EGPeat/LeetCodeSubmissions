class Solution:
    def numDecodings(self, s: str) -> int:
        if not s or s[0] == "0":
            return 0
        ways = [0] * (len(s)+1)
        ways[0] = 1
        for i in range(1, len(s)+1):
            if s[i - 1] != '0':
                ways[i] = ways[i - 1]
            if i >= 2 and s[i - 2] != '0' and int(s[i - 2:i]) <= 26:
                ways[i] += ways[i - 2]
        return ways[-1]