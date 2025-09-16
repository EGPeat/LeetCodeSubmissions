# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        sub_spot = find_sub_spot(root, subRoot)
        if not sub_spot:
            return False
        return isSameTree(sub_spot, subRoot)

def find_sub_spot(root, subroot):
    if not root:
        return None
    if root.val == subroot.val:
        return root
    left = find_sub_spot(root.left, subroot)
    right = find_sub_spot(root.right, subroot)
    if left and left.val == subroot.val:
        return left
    elif right and right.val == subroot.val:
        return right
    else:
        return None
   

def isSameTree(p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        elif not p and q or p and not q:
            return False
        elif p.val != q.val:
            return False
        left_true = isSameTree(p.left, q.left)
        right_true =  isSameTree(p.right, q.right)
        return min(left_true, right_true) 