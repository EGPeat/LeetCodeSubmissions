"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return
        result = []
        second_previous = None
        queue = deque()
        queue.append(root)
        while queue:
            levelSize = len(queue)

            temp_val = 0
            previous = None
            for _ in range(levelSize):
                node = queue.popleft()
                if previous:
                    previous.next = node
                previous = node

                if node.left is not None:
                    queue.append(node.left)

                if node.right is not None:
                    queue.append(node.right)

        return root