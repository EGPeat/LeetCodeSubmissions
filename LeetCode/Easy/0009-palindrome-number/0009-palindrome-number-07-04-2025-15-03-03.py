class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x is None:
            return False
        if x < 0:
            return False
        list_x = list(str(x))
        if len(list_x) == 1:
            return True
        while len(list_x) > 1:
            if list_x[0] != list_x[-1]:
                return False
            list_x.pop(0)
            list_x.pop(-1)
        return True