# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        paths = []
        self.binary_helper(root, paths, temp=[])
        paths_out = []
        for path in paths:
            temp_str = ""
            for item in path:
                temp_str += f"{item}->"
            paths_out.append(temp_str[:-2])
        return paths_out

    def binary_helper(self, root, paths, temp):
        temp.append(root.val)
        if root.left:
            self.binary_helper(root.left, paths, temp)
        if root.right:
            self.binary_helper(root.right, paths, temp)
        if not root.left and not root.right:
            paths.append(temp.copy())
        temp.pop()
    