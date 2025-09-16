# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.sum_val = 0
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        if root:
            self.helper(root, low, high)
            return self.sum_val
    def helper(self, root, l, h):
        if not root:
            return
        self.helper(root.left, l, h)
        if l <= root.val <= h:
            self.sum_val += root.val
        self.helper(root.right, l, h)