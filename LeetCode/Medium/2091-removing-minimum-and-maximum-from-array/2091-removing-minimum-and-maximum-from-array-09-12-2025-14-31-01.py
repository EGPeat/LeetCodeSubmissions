class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        min_loc, max_loc = nums.index(min(nums)), nums.index(max(nums))
        min_to_max = abs(min_loc - max_loc)
        end_to_min = len(nums) - min_loc
        end_to_max = len(nums) - max_loc
        pair1min = min(max(end_to_max, end_to_min), end_to_min+max_loc + 1)
        pair2min = min(end_to_max+min_loc + 1, min_loc + max_loc + 2)
        end_to_both = max(end_to_max, end_to_min)
        start_to_both = min(min_loc + min_to_max + 1, max_loc + min_to_max + 1)
        min_filtering1 = min(pair1min, pair2min)
        min_filtering2 = min(end_to_both, start_to_both)
        return min(min_filtering1, min_filtering2)