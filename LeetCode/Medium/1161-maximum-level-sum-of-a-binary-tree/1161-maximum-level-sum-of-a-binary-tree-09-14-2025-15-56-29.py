# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        max_val = [float("-inf"), 0]

        queue = deque()
        queue.append(root)
        depthval = 0
        while queue:
            depthval += 1
            levelSize = len(queue)

            temp_val = 0
            for _ in range(levelSize):
                node = queue.popleft()
                print(node.val, end=" ")
                temp_val += node.val

                if node.left is not None:
                    queue.append(node.left)

                if node.right is not None:
                    queue.append(node.right)
            if temp_val > max_val[0]:
                max_val = [temp_val, depthval]

        return max_val[1]
