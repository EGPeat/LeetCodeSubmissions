# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        def search(root):
            if not root:
                return (0, True)
            left_side = search(root.left)
            right_side = search(root.right)
            if abs(left_side[0] - right_side[0]) < 2 and left_side[1] and right_side[1]:
                return (1 + max(left_side[0], right_side[0]), True)
            else:
                return (1 + max(left_side[0], right_side[0]), False)
        
        left_side = search(root.left)
        right_side = search(root.right)
        if abs(left_side[0] - right_side[0]) < 2 and left_side[1] and right_side[1]:
            return True
        else:
            return False