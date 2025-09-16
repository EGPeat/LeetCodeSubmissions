# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        return self.symhelper(root.left, root.right) if root else True

    def symhelper(self, left, right):
        if not left and not right:
            return True
        elif (not left and right) or (left and not right):
            return False
        elif left.val != right.val:
            return False
        left_test = self.symhelper(left.left, right.right)
        right_test = self.symhelper(left.right, right.left)


        return min(left_test, right_test)
