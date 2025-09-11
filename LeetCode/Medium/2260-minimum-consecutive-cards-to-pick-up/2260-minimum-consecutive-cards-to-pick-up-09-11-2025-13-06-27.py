class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        curr_dict = {}
        length = len(cards) + 2#need to do end - len(check)
        start = 0
        for end in range(len(cards)):
            curr_dict[cards[end]] = curr_dict.get(cards[end], 0) + 1
            while curr_dict[cards[end]] >= 2:
                length = min(length, end - start + 1)
                curr_dict[cards[start]] = curr_dict.get(cards[start], 0) - 1
                start += 1

        if length != len(cards) + 2:
            return length
        return -1