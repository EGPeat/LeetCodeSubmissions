class Solution:
    def myAtoi(self, s: str) -> int:
        #print(f"#{s}#")
        s = s.strip()
        #print(f"#{s}#")
        output = 0
        neg_mult = False
        for i, char in enumerate(s):
            #print(i, char, output)
            if i ==  0 and char == "-":
                neg_mult = True
            elif i == 0 and char == "+":
                pass
            elif char in "0123456789":
                output *= 10
                output += int(char)
            else:
                break
                
            #elif char
        
        #print(output)
        
        if not output:
            return 0
        if neg_mult:
            output *= -1
        if output < -pow(2, 31):
            output = -pow(2, 31)
        if output > (pow(2, 31)-1):
            output = (pow(2, 31)-1)
        return output 