class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        pre = 0
        pre_dict = defaultdict(int)
        pre_dict[0] = 1
        count = 0
        for i, val in enumerate(nums):
            pre += val
            if pre-k in pre_dict.keys():
                count += pre_dict[pre-k]

            pre_dict[pre] += 1

        return count