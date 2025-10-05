class Solution:
    def addMinimum(self, word: str) -> int:
        count = 0
        word = word.replace("abc", "x")
        stack = []
        for char in word:
            if char != "x":
                stack.append(char)
            elif stack:
                stack.pop()
                count += 2
            #print(stack, count)

            if len(stack) >= 2:
                if stack[-1] == stack[-2]:
                    count += 2
                    stack.pop()
                elif stack[-1] == "a":
                    count += 2
                    stack.pop()
                    stack.pop()
                    stack.append("a")
                elif (stack[-2] == "a" and stack[-1] == "b") or (stack[-2] == "a" and stack[-1] == "c") or (stack[-2] == "b" and stack[-1] == "c"):
                    count += 1
                    stack.pop()
                    stack.pop()
        if stack:
            count += 2 * len(stack)
        return count