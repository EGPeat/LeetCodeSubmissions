class Solution:
    def __init__(self):
        self.prev = -float('inf')
    def inorder_traversal(node):
            if node is None:
                return True
            if not inorder_traversal(node.left):
                return False
            if self.prev >= node.val:
                return False
            self.prev = node.val
            return inorder_traversal(node.right)

    def isValidBST(self, root: TreeNode) -> bool:
        return self.inorder_traversal(root)
