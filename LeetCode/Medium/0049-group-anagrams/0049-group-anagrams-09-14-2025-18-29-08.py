from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs):
        output = []
        string_dict = defaultdict(list)
        for string in strs:
            temp_dict = {}
            for char in string:
                temp_dict[char] = temp_dict.get(char, 0) + 1
            temp_dict = dict(sorted(temp_dict.items()))
            string_dict[str(temp_dict)].append(string)

        for key, value in string_dict.items():
            output.append(value)

        return output
