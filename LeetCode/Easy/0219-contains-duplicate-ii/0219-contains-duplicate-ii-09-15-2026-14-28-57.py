class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        num_dict = {}
        for idx, number in enumerate(nums):
            if number in num_dict and abs(idx-num_dict[number]) <= k:
                return True
            else:
                num_dict[number] = idx
        return False

