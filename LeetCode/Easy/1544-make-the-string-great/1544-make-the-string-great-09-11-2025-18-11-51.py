class Solution:
    def makeGood(self, s: str) -> str:
        stack = []
        for char in s:
            diff_case = False
            if stack and char.islower() != stack[-1].islower():
                diff_case = True
            if stack and char.lower() == stack[-1].lower() and diff_case:
                stack.pop()
            else:
                stack.append(char)
        return "".join(stack)