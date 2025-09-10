class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ans = ""
        counter = -1
        while True: #add condition to kill when reached end of smallest string
            counter += 1
            theset = set()
            for the_string in strs:
                if counter < len(the_string):
                    theset.add(the_string[counter])
                    if len(theset) > 1:
                        return ans
                else:
                    return ans
            ans += next(iter(theset))
