class Solution:
    def backspaceCompare(self, str1: str, str2: str) -> bool:
        phrase1 = self.reduction(str1)
        phrase2 = self.reduction(str2)
        if phrase1 == phrase2:
            return True
        return False

    def reduction(self, str1):
        phrase = []
        p1 = len(str1) - 1
        skip_count = 0
        while p1 >= 0:
            while str1[p1] == "#" and p1 >= 0:
                skip_count += 1
                p1 -= 1
            while skip_count > 0 and p1 >= 0 and str1[p1] != "#":
                p1 -= 1
                skip_count -= 1
            if str1[p1] != "#" and p1 >= 0:
                phrase.append(str1[p1])
                p1 -= 1
        return phrase