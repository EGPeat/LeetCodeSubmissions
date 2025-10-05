class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        lister = [(idx, item) for idx, item in enumerate(s) if item in "()"]
        if len(lister) == 0:
            return s
        lister = lister[::-1]
        stack = []
        remove = []
        while lister:
            temp = lister.pop()
            if temp[1] == ")" and not stack:
                remove.append(temp[0])
            elif temp[1] == ")" and stack:
                stack.pop()
            else:
                stack.append(temp)
        for item in stack:
            remove.append(item[0])
        remove.sort(reverse=True)
        for item in remove:
            s = s[:item] + s[item+1:]
        return s