class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        temp = []
        candidates.sort()
        res = self.combo_helper(candidates, target, temp, res)
        return res

    def combo_helper(self, candidates, target, temp, res):
        for option in candidates:
            if 0 < target:
                if temp and option >= temp[-1] or not temp:
                    temp.append(option)
                    res = self.combo_helper(candidates, target-option, temp, res)
                    temp.remove(option)
            if target == 0:
                if temp not in res:
                    res.append(temp.copy())
        return res
