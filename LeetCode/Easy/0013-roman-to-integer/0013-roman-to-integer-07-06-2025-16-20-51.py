class Solution:
    def romanToInt(self, s: str) -> int:
        conversion_dict = {
            'M': 1000, 'D': 500, 'C': 100, 
            'L': 50, 'X':10, 'V': 5, 'I': 1
            }
        temp_str = ''
        temp_number = 0
        for i in range(1, len(s) + 1):
            new_val = s[-i]
            
            if temp_str:
                if (new_val != temp_str[-1]) & (conversion_dict[new_val] < conversion_dict[temp_str[-1]]):
                    temp_number += (len(temp_str) * conversion_dict[temp_str[-1]]) - conversion_dict[new_val]
                    temp_str = ''
                elif new_val != temp_str[-1]:
                    temp_number += len(temp_str) * conversion_dict[temp_str[-1]]
                    temp_str = ''
                    temp_str += new_val
                else:
                    temp_str += new_val
            else:
                temp_str += new_val
        temp_number += len(temp_str) * conversion_dict[temp_str[-1]]
        return temp_number