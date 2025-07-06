class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        hash_table = {}
        longest_substring = ''
        for string in strs:
            for idx in range(len(string)+1):
                hash_table[string[0:idx]] = hash_table.get(string[0:idx], 0) + 1
        
        for idx in range(len(strs[0])+1):
            sub_section = strs[0][0:idx]
            hash_val = hash_table[strs[0][0:idx]]
            if hash_val == len(strs) and len(sub_section) >= len(longest_substring):
                longest_substring = sub_section
        return longest_substring