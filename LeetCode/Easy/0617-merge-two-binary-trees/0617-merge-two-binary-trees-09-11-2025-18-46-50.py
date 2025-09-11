# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, t1: Optional[TreeNode], t2: Optional[TreeNode]) -> Optional[TreeNode]:
        if not t1 and not t2:
            return None
        elif not t1:
            return t2
        elif not t2:
            return t1
        elif t1 and t2:
            left_val = self.mergeTrees(t1.left, t2.left)
            right_val = self.mergeTrees(t1.right, t2.right)

        

        if t2 and t1:
            t1.val = t1.val + t2.val

        if not t1.left and t2.left:
            t1.left = t2.left
        if not t1.right and t2.right:
            t1.right = t2.right

        return t1