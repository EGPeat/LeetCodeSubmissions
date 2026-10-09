# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: TreeNode | None) -> list[int]:
        dic = dict()
        self.find_helper(root, dic)
        max_val = max(dic.values())
        output = []
        for k,v in dic.items():
            if v == max_val:
                output.append(k)
        return output

    def find_helper(self, root, dic):

        if not root:
            return
        self.find_helper(root.left, dic)
        self.find_helper(root.right, dic)
        dic[root.val] = dic.get(root.val, 0) + 1