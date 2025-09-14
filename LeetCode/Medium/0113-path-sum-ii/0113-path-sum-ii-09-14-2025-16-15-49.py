# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root, sum_val):
        allPaths = []
        self.findPaths_recursive(root, sum_val, allPaths, [])
        return allPaths

    def findPaths_recursive(self, root, sum_val, allPaths, pathway=[]):
        if root is None:
            return None
        pathway.append(root.val)

        if root.left is None and root.right is None and root.val == sum_val:
            allPaths.append(list(pathway))
        else:
            left_path = self.findPaths_recursive(
                root.left, sum_val - root.val, allPaths, pathway
            )
            right_path = self.findPaths_recursive(
                root.right, sum_val - root.val, allPaths, pathway
            )
        del pathway[-1]
