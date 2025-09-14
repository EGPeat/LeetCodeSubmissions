class Solution:
    def amount_too_large(self, dict_count, letter_set, k):
        max_val = dict_count[1]
        sum_val = -max_val
        for letter in letter_set:
            sum_val += dict_count[letter]
        if sum_val > k:
            return True
        else:
            return False

    def longestSubarray(self, arr):
        k = 1
        max_length = 0
        dict_count = {0: 0, 1: 0}

        letter_set = set()

        start = 0
        for idx, char in enumerate(arr):
            letter_set.add(char)

            dict_count[char] = dict_count.get(char, 0) + 1
            print(dict_count)

            if self.amount_too_large(dict_count, letter_set, k):
                max_length = max(
                    max_length, idx - start
                )  # no +1 to ignore the bad character
            while self.amount_too_large(dict_count, letter_set, k):
                dict_count[arr[start]] = dict_count.get(arr[start], 0) - 1
                if dict_count[arr[start]] == 0:
                    letter_set.remove(arr[start])
                start += 1

        max_length = max(max_length, len(arr) - start)
        return max_length - 1
