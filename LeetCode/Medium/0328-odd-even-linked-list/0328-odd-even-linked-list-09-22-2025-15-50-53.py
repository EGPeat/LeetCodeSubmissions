# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        n1 = head
        n2 = head.next
        n2copy = n2
        while n1 and n2:
            if n1.next and n1.next.next:
                n1.next = n1.next.next
            else:
                n1.next = None
            if n2.next and n2.next.next:
                n2.next = n2.next.next
            else:
                n2.next = None
            n1old = n1
            n1 = n1.next
            n2 = n2.next
        if n1:
            n1.next = n2copy
        else:
            n1old.next = n2copy
        return head