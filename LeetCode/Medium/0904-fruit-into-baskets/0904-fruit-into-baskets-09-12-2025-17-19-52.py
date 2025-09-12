class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        max_length = 0
        dict_count = {}
        letter_set = set()

        start = 0
        for idx, char in enumerate(fruits):
            letter_set.add(char)
            if len(letter_set) > 2:
                max_length = max(
                    max_length, idx - start
                )  # no +1 to ignore the bad character
            dict_count[char] = dict_count.get(char, 0) + 1
            while len(letter_set) > 2:
                dict_count[fruits[start]] = dict_count.get(fruits[start], 0) - 1
                if dict_count[fruits[start]] == 0:
                    letter_set.remove(fruits[start])
                start += 1

        max_length = max(max_length, len(fruits) - start)
        return max_length