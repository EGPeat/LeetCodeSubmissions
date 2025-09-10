class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x is None:
            return False
        if x < 0:
            return False
        if x < 10:
            return True
        list_x = list(str(x))
        len_num = len(list_x)
        for i in range(len_num//2):
            if list_x[i] != list_x[len_num-i-1]:
                return False
        return True


class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x is None:
            return False
        if x < 0:
            return False
        list_x = list(str(x))
        if len(list_x) == 1:
            return True
        len_num = len(list_x)
        for i in range(len_num//2):
            if list_x[i] != list_x[len_num-i-1]:
                return False
        return True