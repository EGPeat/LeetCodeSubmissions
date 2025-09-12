# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverse(self, head):
        prev = None
        while (head is not None):
            next = head.next
            head.next = prev
            prev = head
            head = next
        return prev


    def reorderList(self, head):
        fast = head
        slow = head

        while fast is not None and fast.next:
            fast = fast.next.next
            slow = slow.next
        slow2 = head
        middle = slow
        head_second_half = self.reverse(slow)  # reverse the second half

        while (slow2 is not None and head_second_half is not None):
            if slow == head_second_half:
                break
            third_place = slow2.next
            second_place = head_second_half
            first_place = slow2
            head_second_half = head_second_half.next
            slow2 = slow2.next

            first_place.next = second_place
            second_place.next = third_place


