class Solution:
    def operation(self, a, b, type):
        match type:
            case "/":
                return math.trunc(a / b)
            case "+":
                return a + b
            case "-":
                return a - b
            case "*":
                return a * b

    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        first = True
        for tok in tokens:
            if tok in "/*+-":
                num = int(stack.pop())
                num2 = int(stack.pop())
                if tok == "+":
                    stack.append(num + num2)
                elif tok == "*":
                    stack.append(num * num2)
                elif tok == "-":
                    stack.append(num2 - num)
                elif tok == "/":
                    stack.append(math.trunc(num2 / num))
            else:
                stack.append(tok)
        if stack:
            return int(stack[0])
        return temp_num