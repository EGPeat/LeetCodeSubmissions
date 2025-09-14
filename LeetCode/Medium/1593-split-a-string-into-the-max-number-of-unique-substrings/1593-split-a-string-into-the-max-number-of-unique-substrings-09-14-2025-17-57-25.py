class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        if not s:
            return 0
        temp_list = []
        best_len = self.splitter_helper([], 0, 0, s)
        return best_len

    def splitter_helper(self, array_list, curr_start, curr_loc, s):
        if curr_loc == len(s):
            if curr_start == curr_loc:
                return len(array_list)
            else:
                return 0
        len2 = self.splitter_helper(array_list.copy(), curr_start, curr_loc + 1, s)
        if s[curr_start : curr_loc + 1] not in array_list:
            array_list.append(s[curr_start : curr_loc + 1])
            len1 = self.splitter_helper(
                array_list.copy(), curr_loc + 1, curr_loc + 1, s
            )
            return max(len1, len2)
        return len2
