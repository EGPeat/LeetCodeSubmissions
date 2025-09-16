class Solution:
    def reverseBits(self, n: int) -> int:
        stack = []
        while n >= 1:
            stack.append((n%2))
            n //= 2
        while len(stack) < 32:
            stack.append(0)
        num = 0
        power = 0
        while stack:
            temp = stack.pop()
            num += temp * pow(2, power)
            power += 1

        return num