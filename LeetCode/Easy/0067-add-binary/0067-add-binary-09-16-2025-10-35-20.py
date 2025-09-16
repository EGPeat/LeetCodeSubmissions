class Solution:
    def addBinary(self, a: str, b: str) -> str:
        c = ""
        a_len = len(a)
        b_len = len(b)
        a = a[::-1]
        b = b[::-1]
        carry = 0
        for i in range(max(a_len, b_len)):
            ai, bi = 0, 0
            if i < a_len:
                ai = int(a[i])
            if i < b_len:
                bi = int(b[i])
            #print(c, ai, ai, carry, ai + bi + carry)
            num = ai + bi + carry
            carry = num // 2
            c+= str(num%2)
        if carry:
            c += str(carry)
        return c[::-1]