class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_reachable = 0
        for current_pos, jump_length in enumerate(nums):
            if max_reachable < current_pos:
                return False
            max_reachable = max(max_reachable, current_pos + jump_length)
        return True