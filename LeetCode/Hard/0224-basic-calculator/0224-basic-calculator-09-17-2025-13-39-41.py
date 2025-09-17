class Solution:

    def calculate(self, s: str) -> int:
        s = s.replace(" ", "")
        curr_num = 0
        string_length = len(s)
        prev_op = '+'
        stack = []
        temp_num = 0
        #print(s)
        for index, tok in enumerate(s):
            #print(stack)
            if tok.isdigit():
                curr_num = curr_num * 10 + int(tok)
            if tok == ")":
                if prev_op == "+":
                    stack.append(curr_num)
                elif prev_op == "-":
                    stack.append(-curr_num)
                
                prev_op = "+"
                curr_num = 0

                #print(f"stack at ) is {stack} and tempnum is {temp_num} and curr_num is {curr_num}")
                temp = stack.pop()
                while temp != "(":  
                    temp_num += temp
                    temp = stack.pop()
                temp = stack.pop()
                temp_num *= temp
                stack.append(temp_num)
                temp_num = 0
            if tok == "(": #doesn't respect - before ()
                if prev_op is "-":
                    stack.append(-1)
                if prev_op is "+":
                    stack.append(1)
                stack.append(tok)
                prev_op = "+"
            if index == string_length - 1 or tok in '+-*/':
                if prev_op == "+":
                    stack.append(curr_num)
                elif prev_op == "-":
                    stack.append(-curr_num)
                
                prev_op = tok
                curr_num = 0
        #print(f"here we are at the end", stack)
        temp_num = 0
        while stack:
            #print(temp_num, stack)
            temp = stack.pop()
            if temp == "+":
                pass
            elif temp == "-":
                temp_num *= -1
            else:
                temp_num += temp
        #print(temp_num)
        return temp_num