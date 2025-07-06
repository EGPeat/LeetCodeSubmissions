class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        until_three = set()
        while True:
            for number in nums:
                if number not in until_three:
                    until_three.add(number)
                    if len(until_three) >= 3:
                        break
            if len(until_three) < 3:
                max_num = max(until_three)
                return max_num
            break
    
        first_max = -2147483648
        second_max = -2147483648
        third_max = -2147483648

        for number in nums:
            if number > first_max:
                third_max = second_max
                second_max = first_max
                first_max = number
            elif number > second_max and number < first_max:
                third_max = second_max
                second_max = number
            elif number > third_max and number < second_max:
                third_max = number
        return third_max