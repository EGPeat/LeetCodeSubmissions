# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        output = []
        self.preorder_helper(root, output)
        print(output)
        return output

    def preorder_helper(self, root, output):
        if root:
            output.append(root.val)
            self.preorder_helper(root.left, output)
            self.preorder_helper(root.right, output)