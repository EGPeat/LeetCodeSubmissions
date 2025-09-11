class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        count = 0
        jewels_set = set(jewels)
        for item in stones:
            if item in jewels:
                count += 1
        return count