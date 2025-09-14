class Solution:
    def subarraysDivByK(self, nums, k):
        cum_map = {0: 1}
        cum_sum = 0
        max_len = 0

        for i in range(len(nums)):
            cum_sum += nums[i]

            if (cum_sum % k) in cum_map:
                max_len += cum_map[cum_sum % k]
                cum_map[cum_sum % k] += 1

            if cum_sum % k not in cum_map:
                cum_map[cum_sum % k] = 1

        return max_len
