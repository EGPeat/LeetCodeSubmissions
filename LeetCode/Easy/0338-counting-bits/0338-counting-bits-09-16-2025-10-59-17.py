class Solution:
    def countBits(self, n: int) -> List[int]:
        if n == 0:
            return [0]
        elif n == 1:
            return [0, 1]
        out = [0] * (n + 1)
        two_mult = 2
        #out[1] = 1
        i = 0
        while 2 * i <= n or 2 * i + 1 <= n:
            if 2 * i <= n:
                out[2 * i] = out[i]
            if 2 * i + 1 <= n:
                out[2 * i + 1] = out[i] + 1
            i += 1
        
        return out