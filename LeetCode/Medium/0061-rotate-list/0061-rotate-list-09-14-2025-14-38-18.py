# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], rotations: int) -> Optional[ListNode]:
        if not head:
            return head
        head_copy = head
        length = 1
        while head_copy.next:
            head_copy = head_copy.next
            length += 1

        moves_right = rotations % length
        if moves_right == 0:
            return head
        moves_until_replacement_head = length - moves_right
        head_copy = head
        replacement_head = None
        end_of_replacement_section = None
        replacement_tail = None
        end_of_replacement_tail = None

        for idx in range(moves_until_replacement_head - 1):
            head_copy = head_copy.next
        new_tail_maybe = head_copy
        replacement_head = head_copy.next
        for idx in range(moves_right):
            head_copy = head_copy.next
        end_of_replacement_section = head_copy
        new_tail_maybe.next = None
        end_of_replacement_section.next = head
        return replacement_head
