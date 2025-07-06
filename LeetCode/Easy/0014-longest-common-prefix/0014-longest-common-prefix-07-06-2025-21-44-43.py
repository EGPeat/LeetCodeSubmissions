class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        for idx in range(len(strs[0])+1):
            sub_section = strs[0][0:idx]
            for string in strs[1:]:
                if not string[0:idx].startswith(sub_section):
                    return strs[0][0:idx-1]
        return strs[0]