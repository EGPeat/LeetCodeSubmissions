class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) < 2:
            return False
        starter = ["(", '{', "["]
        finisher = [")", "}", "]"]
        stack = []
        s_list = list(s)
        
        while True:
            if len(s_list) == 0:
                break
            temp = s_list.pop(0)
            if temp in starter:
                stack.append(temp)
            if temp in finisher:
                if len(stack) == 0:
                    return False
                matching = stack.pop()
                loc = finisher.index(temp)
                if starter.index(matching) != loc:
                    return False
        if len(stack) > 0:
            return False
        return True