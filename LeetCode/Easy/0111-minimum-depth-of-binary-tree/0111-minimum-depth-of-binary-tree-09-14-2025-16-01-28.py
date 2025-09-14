# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        minimumTreeDepth = 0
        queue = deque()
        queue.append(root)
        while queue:
            minimumTreeDepth += 1
            levelSize = len(queue)

            temp_val = 0
            for _ in range(levelSize):
                node = queue.popleft()
                temp_val += node.val
                if node.left is None and node.right is None:
                    return minimumTreeDepth
                if node.left is not None:
                    queue.append(node.left)

                if node.right is not None:
                    queue.append(node.right)

        return minimumTreeDepth
