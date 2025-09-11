class Solution:
    def findAnagrams(self, original: str, check: str) -> List[int]:
        check_len = len(check)
        check_dict = {}
        curr_dict = {}
        locs = [] #need to do end - len(check)
        for c in check:
            check_dict[c] = check_dict.get(c, 0) + 1
        
        for end in range(len(original)):
            curr_dict[original[end]] = curr_dict.get(original[end], 0) + 1
            if end >= check_len:
                check_dict[original[end-check_len]] = check_dict.get(original[end-check_len], 0) + 1
            if check_dict == curr_dict:
                locs.append(end - check_len + 1)
        return locs