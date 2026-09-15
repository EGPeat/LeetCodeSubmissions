class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        ranges = []
        for idx, item in enumerate(nums):
            if not (ranges and item <= ranges[-1][1]):
                r_start = item
                r_end = item
                i = 1
                while idx + i < len(nums) and nums[idx+i] == nums[idx+i-1] + 1:
                    r_end = nums[idx+i]
                    i+=1
                ranges.append([r_start, r_end])

        #print(ranges)
        ranges_out = []
        for r in ranges:
            if r[0] ==r[1]:
                ranges_out.append(str(r[0]))
            else:
                ranges_out.append(f'{r[0]}->{r[1]}')
        #print(ranges_out)
        return ranges_out