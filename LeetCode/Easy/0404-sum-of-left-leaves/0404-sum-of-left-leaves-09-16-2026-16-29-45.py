# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: TreeNode | None) -> int:
        self.output = 0
        self.lefthelper(root, False)
        return self.output
        
    def lefthelper(self, root, left):
        if left and not root.left and not root.right:
            self.output += root.val
        elif not root.left and not root.right:
            return
        else:
            self.lefthelper(root.left, True) if root.left else None
            self.lefthelper(root.right, False) if root.right else None
