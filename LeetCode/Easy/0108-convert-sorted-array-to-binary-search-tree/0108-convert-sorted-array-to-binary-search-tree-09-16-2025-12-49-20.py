# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if len(nums) == 0:
            return None
        middle = (len(nums))//2
        middle_node = TreeNode(nums[middle])
        middle_node.left = self.sortedArrayToBST(nums[:middle])
        middle_node.right = self.sortedArrayToBST(nums[middle+1:])
        return middle_node
