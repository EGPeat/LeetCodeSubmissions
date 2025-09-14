class Solution:
    def compare_dicts(self, pattern_dict, letter_dict):
        for key in pattern_dict.keys():
            if key not in letter_dict.keys():
                return False
            if pattern_dict[key] > letter_dict[key]:
                return False
        return True

    def minWindow(self, str1, pattern):
        result_indices = []
        best_len = math.inf
        pattern_count = {}
        dict_count = {}
        start = 0
        k = len(pattern)
        for letter in pattern:
            pattern_count[letter] = pattern_count.get(letter, 0) + 1

        for idx, char in enumerate(str1):
            dict_count[char] = dict_count.get(char, 0) + 1
            while (
                str1[start] not in pattern
                or dict_count[str1[start]] > pattern_count[str1[start]]
            ):
                dict_count[str1[start]] = dict_count.get(str1[start], 0) - 1
                start += 1
                if start > idx:
                    break
            if (
                self.compare_dicts(pattern_count, dict_count)
                and (idx - start) < best_len
            ):
                if result_indices:
                    result_indices.pop()
                result_indices.append([start, idx])
                best_len = idx - start
        if best_len != math.inf:
            return str1[result_indices[0][0] : result_indices[0][1] + 1]
        else:
            return ""
