class Solution:
    def romanToInt(self, s: str) -> int:
        conversion_dict = {
            'M': 1000, 'D': 500, 'C': 100, 
            'L': 50, 'X':10, 'V': 5, 'I': 1
            }
        output_number = 0
        memory = 0
        list_str = [conversion_dict[item] for item in list(s)]
        print(list_str)
        while list_str:
            new_number = list_str.pop()
            if new_number < memory:
                output_number -= new_number
            else:
                output_number += new_number
            memory = new_number
        return output_number