# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        previous = None
        current = head
        if head:
            real_next = head.next
            while real_next:
                current.next = previous
                previous = current
                current = real_next
                real_next = current.next
            current.next = previous
        return current