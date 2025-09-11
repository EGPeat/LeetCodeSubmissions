class Solution:
    def removeDuplicates(self, s: str) -> str:
        s_list = list(s)
        stack = []
        for letter in s_list:
            if stack and letter == stack[-1]:
                stack.pop()
            elif stack and letter != stack[-1] or not stack:
                stack.append(letter)
        return "".join(stack)