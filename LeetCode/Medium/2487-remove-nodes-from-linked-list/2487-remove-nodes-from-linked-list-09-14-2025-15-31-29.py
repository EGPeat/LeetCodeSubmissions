# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        decreasing_stack = []
        while head:
            while decreasing_stack and decreasing_stack[-1][0] < head.val:
                decreasing_stack.pop()
            decreasing_stack.append((head.val, head))
            head = head.next
        child = decreasing_stack.pop()
        parent = child
        while decreasing_stack:
            parent = decreasing_stack.pop()
            parent[1].next = child[1]
            child = parent
        return parent[1]