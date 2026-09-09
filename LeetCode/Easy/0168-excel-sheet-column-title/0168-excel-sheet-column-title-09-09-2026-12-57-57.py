class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        outstr = ""
        while columnNumber > 0:
            columnNumber -= 1
            columnNumber, n = divmod(columnNumber, 26)
            print(n, columnNumber)
            outstr += chr(ord('A')+n)

        return outstr[::-1]