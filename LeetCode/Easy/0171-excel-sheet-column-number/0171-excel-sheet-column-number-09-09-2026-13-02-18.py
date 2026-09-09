class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        tmp = 0
        for char in columnTitle:
            tmp = (tmp * 26) + (ord(char) - ord("A")+1)
        return tmp