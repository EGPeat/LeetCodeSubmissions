class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        self.output = set()
        self.helper("()", n-1)
        return list(self.output)

    def helper(self, string, n):
        if n == 0:
            self.output.add(string)
            return
        for i in range(len(string)+1):
            """print(i)
            print(string[:i] + "()" + string[i:])
            print(string[:i], string[i:])
            print("#############")"""
            self.helper(string[:i] + "()" + string[i:], n -1)
