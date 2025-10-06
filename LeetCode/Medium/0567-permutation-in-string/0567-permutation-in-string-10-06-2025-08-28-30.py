class Solution:
    def compare_dicts(self, pattern_dict, letter_dict):
        #print(pattern_dict, letter_dict)
        for key in pattern_dict.keys():
            if key not in letter_dict.keys():
                return False
            if letter_dict[key] < pattern_dict[key]:
                return False
        return True

    def checkInclusion(self, pattern, str1):
        pattern_count = {}
        dict_count = {}
        start = 0
        k = len(pattern)
        for letter in pattern:
            pattern_count[letter] = pattern_count.get(letter, 0) + 1

        for idx, char in enumerate(str1):
            dict_count[char] = dict_count.get(char, 0) + 1
            if (idx - start) + 1 > k:
                dict_count[str1[start]] = dict_count.get(str1[start], 0) - 1
                if dict_count[str1[start]] == 0:
                    del dict_count[str1[start]]
                start += 1

            if self.compare_dicts(pattern_count, dict_count):
                return True
        return False
