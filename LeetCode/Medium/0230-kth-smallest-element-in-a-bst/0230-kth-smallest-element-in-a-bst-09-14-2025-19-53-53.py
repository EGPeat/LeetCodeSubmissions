# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.count = 0
        self.result = 0
        return self.kthSmallestHelper(root, k)
    def kthSmallestHelper(self, root: TreeNode, k: int) -> int:
        if not root or self.count == k:
            return self.result

        left_side = self.kthSmallestHelper(root.left, k)
        self.count += 1
        if self.count == k:
            self.result = root.val
            return self.result
        right_side = self.kthSmallestHelper(root.right, k)
        return self.result
