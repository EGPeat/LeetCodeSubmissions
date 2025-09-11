# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        from collections import deque
        res = []
        queue = deque([root])  # at least one element in the queue to kick start bfs
        l = True
        while len(queue) > 0:  # as long as there is element in the queue
            n = len(queue)  # number of nodes in current level, see explanation above
            new_level = []
            for _ in range(n):  # dequeue each node in the current level
                if l:
                    node = queue.popleft()
                else:
                    node = queue.pop()
                new_level.append(node.val)
                if not l:
                    for child in [node.right, node.left]:  # enqueue non-null children
                        if child is not None:
                            queue.appendleft(child)
                if l:
                    for child in [node.left, node.right]:  # enqueue non-null children
                        if child is not None:
                            queue.append(child)
                            
            res.append(new_level)
            l = not l

        return res