# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        h, l = n, 0

        while l <= h:
            m = l + (h-l)//2
            is_m_bad = isBadVersion(m)
            if m > 0 and is_m_bad and not isBadVersion(m - 1):
                return m
            elif is_m_bad:
                h = m - 1
            elif not is_m_bad:
                l = m + 1
        