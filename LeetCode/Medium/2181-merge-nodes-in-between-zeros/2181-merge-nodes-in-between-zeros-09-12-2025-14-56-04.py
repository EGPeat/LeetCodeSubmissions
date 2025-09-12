# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        head_copy = head
        prev = head
        while head.next:
            while head.next.val != 0:
                head.val += head.next.val
                head.next = head.next.next
            prev = head
            head = head.next
        prev.next = None
        return head_copy