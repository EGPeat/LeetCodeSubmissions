from heapq import *


class Solution:
    def reorganizeString(self, str1):
        char_dict = {}
        heap = []
        output_str = []
        for char in str1:
            char_dict[char] = char_dict.get(char, 0) + 1
        for key, value in char_dict.items():
            heappush(heap, (-value, key))

        while heap:
            tmp1 = heappop(heap)  # make sure to -1
            if output_str and heap and tmp1[1] == output_str[-1]:
                tmp2 = heappop(heap)
                output_str.append(tmp2[1])
                heappush(heap, tmp1)
                if abs(tmp2[0]) != 1:
                    heappush(heap, (tmp2[0] + 1, tmp2[1]))  # is minus 1, since negative
            elif output_str and not heap and tmp1[1] == output_str[-1]:
                return ""
            else:
                output_str.append(tmp1[1])
                if abs(tmp1[0]) != 1:
                    heappush(heap, (tmp1[0] + 1, tmp1[1]))  # is minus 1, since negative
        return "".join(output_str)
