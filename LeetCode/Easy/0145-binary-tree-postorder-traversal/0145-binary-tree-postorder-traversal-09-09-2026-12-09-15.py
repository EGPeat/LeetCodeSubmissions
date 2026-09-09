# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        output = []
        self.postorder_helper(root, output)
        return output

    def postorder_helper(self, root, output):
        if root:
            self.postorder_helper(root.left, output)
            self.postorder_helper(root.right, output)
            output.append(root.val)