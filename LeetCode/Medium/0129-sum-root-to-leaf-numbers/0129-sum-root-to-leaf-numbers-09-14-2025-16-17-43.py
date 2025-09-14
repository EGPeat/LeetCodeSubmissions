# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        allPaths = []
        self.findPaths_recursive(root, allPaths, [])
        allPaths = [int(num) for num in allPaths]

        return sum(allPaths)

    def findPaths_recursive(self, root, allPaths, pathway=[]):
        if root is None:
            return None
        pathway.append(root.val)

        if root.left is None and root.right is None:
            new_number = "".join(map(str, pathway))
            allPaths.append(new_number)
        else:
            left_path = self.findPaths_recursive(root.left, allPaths, pathway)
            right_path = self.findPaths_recursive(root.right, allPaths, pathway)
        del pathway[-1]
