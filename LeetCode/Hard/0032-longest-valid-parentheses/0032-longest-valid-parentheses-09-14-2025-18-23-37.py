class Solution:
    def longestValidParentheses(self, s: str) -> int:
        max_length = 0
        stack = [-1]

        for idx, char in enumerate(s):
            if char == "(":
                stack.append(idx)
            elif char == ")":
                stack.pop()
                if not stack:
                    stack.append(idx)
                else:
                    max_length = max(max_length, idx - stack[-1])
        return max_length
