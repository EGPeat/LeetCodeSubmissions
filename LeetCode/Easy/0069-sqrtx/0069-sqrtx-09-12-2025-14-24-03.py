class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0
        if x <= 3:
            return 1
        start = 2
        end = x//2
        while start <= end:
            mid = start + (end - start) // 2
            if (mid*mid) <= x and (mid+1)*(mid+1) > x:
                return int(mid)
            elif (mid*mid) <= x and (mid+1)*(mid+1) <= x:
                start = mid + 1
            elif mid*mid >= x and (mid+1)*(mid+1) >= x:
                end = mid - 1

        return 0