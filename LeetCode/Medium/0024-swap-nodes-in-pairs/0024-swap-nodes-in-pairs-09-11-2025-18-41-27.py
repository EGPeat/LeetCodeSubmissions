# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        previous = dummy
        current = head

        while current and current.next:
            temp = current.next.next
            previous.next = current.next
            previous.next.next = current
            current.next = temp
            previous = current
            current = temp



        return dummy.next