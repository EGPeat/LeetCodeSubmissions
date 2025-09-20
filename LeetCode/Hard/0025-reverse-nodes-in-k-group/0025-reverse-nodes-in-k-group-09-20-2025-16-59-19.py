# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverse_helper(self, head, p, q):
        if p == q:
            return head

        dummy = ListNode(0)
        dummy.next = head
        prev = dummy

        for _ in range(p - 1):
            if prev.next:
                prev = prev.next

        if not prev.next or not prev.next.next:
            return None
        start = prev.next
        then = start.next
        new_start = start

        for _ in range(q - p):
            if new_start.next == None:
                return None
            new_start = new_start.next

        for _ in range(q - p):
            if start.next == None:
                return None
            start.next = then.next
            then.next = prev.next
            prev.next = then
            then = start.next

        return dummy.next

    def reverseKGroup(self, head, k):
        if k < 2:
            return head
        copy_head = head
        k_counter = 0
        while head:
            head = self.reverse_helper(head, 1 + (k * k_counter), k + (k * k_counter))
            if k_counter == 0:
                copy_head = head
            k_counter += 1
        return copy_head