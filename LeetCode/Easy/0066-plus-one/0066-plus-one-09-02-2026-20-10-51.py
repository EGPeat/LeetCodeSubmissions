class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        i = -1
        if digits[i] != 9:
            digits[i] += 1
        else:
            while digits[i] == 9:
                digits[i] = 0
                if i * -1 == len(digits):
                    digits.insert(0, 1)
                    return digits
                i -= 1
            digits[i] += 1
        return digits