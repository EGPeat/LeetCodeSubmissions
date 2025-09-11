class Solution:
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
        maxOnesIdx, maxOnesCount = 0, 0
        for idx in range(len(mat)):
            curr_ones_idx = idx
            curr_ones_count = 0
            for idx2 in range(len(mat[0])):
                if mat[idx][idx2] == 1:
                    curr_ones_count += 1
            if curr_ones_count > maxOnesCount:
                maxOnesIdx = curr_ones_idx
                maxOnesCount = curr_ones_count
        return [maxOnesIdx, maxOnesCount]  