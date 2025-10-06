class Solution:
    def maximumSubarraySum(self, arr: List[int], k: int) -> int:
        result = []
        max_val, start = 0, 0
        numdict = {}
        for end in range(len(arr)):
            numdict[arr[end]] = numdict.get(arr[end], 0) + 1
            max_val += arr[end]
            if end >= (k-1):
                if len(numdict.keys()) == k:
                    result.append(max_val)
                max_val -= arr[start]
                numdict[arr[start]] -= 1
                if numdict[arr[start]] == 0:
                    del numdict[arr[start]]

                start += 1
        if result:
            return max(result)
        return 0