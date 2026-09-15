class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        r = min(len(num1), len(num2))
        lr = max(len(num1), len(num2))
        num1 = num1[::-1]
        num2 = num2[::-1]
        output = []
        carry = 0
        for i in range(r):
            carry,val = divmod(int(num1[i])+int(num2[i])+carry, 10)
            output.append(str(val))
        

        long_num = num1 if len(num1) == lr else num2
        for i in range(r, lr):
            carry,val = divmod(int(long_num[i])+carry, 10)
            output.append(str(val))
        if carry > 0:
            output.append(str(carry))
        output = output[::-1]
        return "".join(output)