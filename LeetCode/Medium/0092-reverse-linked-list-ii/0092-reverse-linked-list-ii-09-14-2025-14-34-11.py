# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head, p, q):
        head_copy = head
        dummy = ListNode(0)
        dummy.next = head
        previous = dummy
        for _ in range(p - 1):
            previous = previous.next

        start = previous.next
        then = start.next

        for _ in range(q - p):
            start.next = then.next
            then.next = previous.next
            previous.next = then
            then = start.next
        return dummy.next
