# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        queue = deque()
        queue.append(root)
        queue.append('x')
        output = []
        temp_out = []
        while queue:
            temp = queue.popleft()
            if temp and temp != "x":
                temp_out.append(temp.val)
                if temp.left:
                    queue.append(temp.left)
                if temp.right:
                    queue.append(temp.right)
            elif temp == "x" and not queue:
                output.append(temp_out)
                temp_out = []
            elif temp == "x":
                queue.append("x")
                output.append(temp_out)
                temp_out = []
        return output
            