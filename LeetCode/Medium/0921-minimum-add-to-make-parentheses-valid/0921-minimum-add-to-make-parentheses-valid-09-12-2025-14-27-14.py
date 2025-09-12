class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        stack = []
        total = 0
        for c in s:
            if c in ['(', '{', '[']:
                stack.append(c)
            else:
                if not stack:
                    total += 1
                if stack:
                    top = stack.pop()
                    if c == ')' and top != '(':
                        total += 1
                    if c == '}' and top != '{':
                        total += 1
                    if c == ']' and top != '[':
                        total += 1
        total += len(stack)
        return total