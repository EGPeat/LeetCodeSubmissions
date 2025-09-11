class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        min_count = float('inf')
        freq = defaultdict(int)
        for idx in range(len(text)):
            freq[text[idx]] += 1

        list_of_balloon = [("b", 1), ("a", 1), ("l", 2), ("o", 2), ("n", 1)]
        for item in list_of_balloon:
            min_count = min(freq[item[0]] // item[1], min_count)

        return min_count