# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        return_list = []
        if root is None:
            return []

        queue = deque()
        queue.append(root)

        while queue:
            levelSize = len(queue)

            temp_list = []
            for _ in range(levelSize):
                node = queue.popleft()
                temp_list.append(node.val)

                if node.left is not None:
                    queue.append(node.left)

                if node.right is not None:
                    queue.append(node.right)
            return_list.append(temp_list)
        return return_list[::-1]
