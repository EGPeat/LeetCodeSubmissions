class Solution:
    def amount_too_large(self, dict_count, letter_set, k):
        max_val = dict_count[max(dict_count, key=dict_count.get)]
        sum_val = -max_val
        for letter in letter_set:
            sum_val += dict_count[letter]
        if sum_val > k:
            return True
        else:
            return False

    def characterReplacement(self, str1, k):
        max_length = 0
        dict_count = {}
        letter_set = set()

        start = 0
        for idx, char in enumerate(str1):
            letter_set.add(char)

            dict_count[char] = dict_count.get(char, 0) + 1
            if self.amount_too_large(dict_count, letter_set, k):
                max_length = max(
                    max_length, idx - start
                )  # no +1 to ignore the bad character
            while self.amount_too_large(dict_count, letter_set, k):
                dict_count[str1[start]] = dict_count.get(str1[start], 0) - 1
                if dict_count[str1[start]] == 0:
                    letter_set.remove(str1[start])
                    del dict_count[str1[start]]
                start += 1

        max_length = max(max_length, len(str1) - start)
        return max_length
