class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        from collections import defaultdict
        maximum = max(nums)
        count = [0] * (maximum + 1)
        count = defaultdict(int)
        count_reversed = defaultdict(list)
        output = [0] * len(nums)
        idx = 0
        for num in nums:
            count[num] += 1
        for key in count.keys():
            count_reversed[count[key]].append(key)
        print(count, count_reversed)
        while count or count_reversed:
            max_val = max(count_reversed)
            max_spot = count_reversed[max_val]
            max_spot.sort(reverse=True)
            #print(max_val, max_spot)
            max_spot = max_spot.pop()
            
            for num in range(max_val):
                output[idx] = max_spot
                idx += 1
            del count[max_spot]
            if not count_reversed[max_val]:
                del count_reversed[max_val]
            print(output)
        output.reverse()
        return output
