class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        s_copy = list(s)
        l_set = set()
        l_dict = {}
        for idx, char in enumerate(s):
            if char in l_dict:
                s_copy[idx] = l_dict[char]
            elif (char not in l_dict) and (t[idx] in l_set):

                
                return False
            else:
                l_dict[char] = t[idx]
                l_set.add(t[idx])
                s_copy[idx] = l_dict[char]
            


        if "".join(s_copy) == t:
            return True
        else:
            return False