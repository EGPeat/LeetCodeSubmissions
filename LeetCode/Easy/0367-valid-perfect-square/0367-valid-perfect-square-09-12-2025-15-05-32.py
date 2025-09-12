class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        return self.perfect_square_calculator(num, 1)
    
    def perfect_square_calculator(self, num, divisor):
        if divisor * divisor == num:
            return True
        elif divisor * divisor > num:
            return False
        return self.perfect_square_calculator(num, divisor+1)