class Solution:
    def isValid(self, s: str) -> bool:
        paren_map = {"(":")", "{":"}", "[":"]"}
        stack_list = []
        for idx in range(len(s)):
            if s[idx] in paren_map.keys():
                stack_list.append(s[idx])
            else:
                if len(stack_list) > 0:
                    if s[idx] == paren_map[stack_list[-1]]:
                        stack_list.pop()
                    else:
                        return False
                else:
                    return False
        if len(stack_list) != 0:
            return False
        else:
            return True