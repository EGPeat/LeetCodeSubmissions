# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.min_difference = float('inf')
        self.prev = -float('inf')
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        if root:
            self.helper(root)
            return self.min_difference
        else:
            return -2
    def helper(self, root):
        if not root:
            return
        self.helper(root.left)
        self.min_difference = min(self.min_difference, root.val - self.prev)
        self.prev = root.val
        self.helper(root.right)
