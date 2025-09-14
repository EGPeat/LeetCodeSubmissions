# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.treeDiameter = 0
        allPaths = []
        self.findPaths_recursive(root, allPaths, [])
        return max(self.treeDiameter - 1, 0)

    def findPaths_recursive(self, root, allPaths, pathway=[]):
        if root is None:
            return []
        pathway.append(root.val)

        temp_pathway = pathway.copy()
        if root.left is None and root.right is None:
            return pathway

        left_path = self.findPaths_recursive(root.left, allPaths, [])
        right_path = self.findPaths_recursive(root.right, allPaths, [])
        if len(left_path) + len(right_path) + 1 > self.treeDiameter:
            self.treeDiameter = len(left_path) + len(right_path) + 1

        if len(pathway) > 0:
            del pathway[-1]

        if len(left_path) > len(right_path):
            left_path.insert(0, root.val)
            return left_path
        else:
            right_path.insert(0, root.val)
            return right_path
