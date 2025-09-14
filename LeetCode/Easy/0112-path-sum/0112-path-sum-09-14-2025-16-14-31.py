# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root, sum_val):
        if root is None:
            return False

        if root.left is None and root.right is None and root.val == sum_val:
            return True
        elif root.left is None and root.right is None:
            return False

        if root.left:
            leftSum = self.hasPathSum(root.left, sum_val - root.val)
        else:
            leftSum = False
        if root.right:
            rightSum = self.hasPathSum(root.right, sum_val - root.val)
        else:
            rightSum = False
        return max(leftSum, rightSum)
