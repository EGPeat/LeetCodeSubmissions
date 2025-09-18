# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:
    def serialize(self, root: TreeNode) -> str:
        if not root:
            return ""
        queue = deque([root])
        output = []
        while queue:
            curr_node = queue.popleft()
            if not curr_node:
                output.append("#")
            else:
                output.append(str(curr_node.val))
                queue.append(curr_node.left)
                queue.append(curr_node.right)

        output2 = ",".join(output)
        return output2

    def deserialize(self, data: str) -> TreeNode:
        if not data:
            return []
        data = data.split(",")
        base_node = TreeNode(int(data[0]))

        queue = deque([base_node])
        idx = 1
        while queue:
            curr_node = queue.popleft()
            if data[idx] != "#":
                curr_node.left = TreeNode(int(data[idx]))
                queue.append(curr_node.left)
            idx += 1
            if data[idx] != "#":
                curr_node.right = TreeNode(int(data[idx]))
                queue.append(curr_node.right)
            idx += 1
        return base_node


# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))