# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def build_subtree(self, preorder, inorder_index_map, preorder_start: int, inorder_start: int, subtree_size: int) -> Optional[TreeNode]:
            if subtree_size <= 0:
                return None
            root_value = preorder[preorder_start]
            root_inorder_index = inorder_index_map[root_value]
            left_subtree_size = root_inorder_index - inorder_start
          

            left_child = self.build_subtree(preorder, inorder_index_map, preorder_start + 1, inorder_start, left_subtree_size)
            right_child = self.build_subtree(preorder, inorder_index_map, preorder_start + 1 + left_subtree_size, root_inorder_index + 1, subtree_size - left_subtree_size - 1)
            return TreeNode(root_value, left_child, right_child)
    
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        inorder_index_map = {value: index for index, value in enumerate(inorder)}
        return self.build_subtree(preorder, inorder_index_map, 0, 0, len(preorder))