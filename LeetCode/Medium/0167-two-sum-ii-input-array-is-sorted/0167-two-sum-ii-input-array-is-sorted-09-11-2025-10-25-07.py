class Solution:
    def twoSum(self, arr: List[int], target: int) -> List[int]:
        l, r = 0, len(arr) - 1
        while l < r:
            comb = arr[l] + arr[r] 
            if comb == target:
                return [l+1, r+1]
            elif comb > target:
                r -= 1
            elif comb < target:
                l += 1
        return []