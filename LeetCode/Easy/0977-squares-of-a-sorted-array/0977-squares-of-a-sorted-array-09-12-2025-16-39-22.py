class Solution:
    def sortedSquares(self, arr: List[int]) -> List[int]:
        n = len(arr)
        squares = [0 for x in range(n)]
        p1 = 0
        p2 = len(arr) - 1
        psquare = len(arr) - 1
        while p1 <= p2:
            p1a = arr[p1]
            p2a = arr[p2]
            if p1a * p1a >= p2a * p2a:
                pass
                squares[psquare] = p1a * p1a
                p1 += 1
                psquare -= 1
            elif p1a * p1a < p2a * p2a:
                squares[psquare] = p2a * p2a
                p2 -= 1
                psquare -= 1
        return squares