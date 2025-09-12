# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        return self.buildMaximumBinaryTreeHelper(nums, 0,  len(nums))
    
    def buildMaximumBinaryTreeHelper(self, nums, start, end):
        print(len(nums), start, end)
        if start >= end:
            return None
        max_val = max(nums[start:end]) #start to end maybe? put in helper func?
        max_loc = nums.index(max_val)
        root = TreeNode(max_val)
        print(nums, max_val, nums[0:nums.index(max_val)])
        print(nums[nums.index(max_val)+1:len(nums)])
        root.left = self.buildMaximumBinaryTreeHelper(nums, start, max_loc)
        root.right = self.buildMaximumBinaryTreeHelper(nums, max_loc + 1, end)
        return root
