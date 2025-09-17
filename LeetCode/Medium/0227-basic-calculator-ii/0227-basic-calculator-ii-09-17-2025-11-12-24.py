class Solution:
    def calculate(self, s: str) -> int:
        s = s.replace(" ", "")
        curr_num = 0
        string_length = len(s)
        prev_op = '+'
        stack = []
        for index, tok in enumerate(s):
            if tok.isdigit():
                curr_num = curr_num * 10 + int(tok)
            if index == string_length - 1 or tok in '+-*/':
                if prev_op == "+":
                    stack.append(curr_num)
                elif prev_op == "-":
                    stack.append(-curr_num)
                elif prev_op == "*":
                    stack.append(stack.pop() * curr_num)
                elif prev_op == "/":
                    stack.append(math.trunc(stack.pop() / curr_num))
                prev_op = tok
                curr_num = 0
        return sum(stack)