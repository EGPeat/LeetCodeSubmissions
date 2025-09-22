class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        prefix = [0] * (len(nums)+1)
        hasher = defaultdict(list)
        hasher[0].append(-1)
        for i, item in enumerate(nums):
            if item == 1:
                prefix[i+1] = prefix[i] + 1
            else:
                prefix[i+1] = prefix[i] - 1
            hasher[prefix[i+1]].append(i)

        best = 0
        for key in hasher.keys():
            best = max(best, hasher[key][-1] - hasher[key][0])
        return best