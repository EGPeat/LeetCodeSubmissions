# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        return self.max_depth_helper(root, 1)
    
    def max_depth_helper(self, root, depth):
        if not root or not root.left and not root.right:
            return depth
        
        depth_left, depth_right = 0, 0
        if root.left:
            depth_left = self.max_depth_helper(root.left, depth + 1)
        if root.right:
            depth_right = self.max_depth_helper(root.right, depth + 1)
        #print(root.val, depth_left, depth_right, depth)
        return max(depth_left, depth_right)
        
        