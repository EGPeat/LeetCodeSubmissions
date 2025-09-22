# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l3 = ListNode()
        l3copy = l3
        carry = 0
        while l1 and l2:
            l3.next = ListNode()
            l3 = l3.next
            val = l1.val + l2.val + carry
            if val >= 10:
                val -= 10
                carry = 1
            else:
                carry = 0
            l3.val = val
            
            l1 = l1.next
            l2 = l2.next
        
        if l1:
            good_list = l1
        elif l2:
            good_list = l2
        else:
            good_list = None
        while good_list:
            l3.next = ListNode()
            l3 = l3.next
            val = good_list.val + carry
            if val >= 10:
                val -= 10
                carry = 1
            else:
                carry = 0
            l3.val = val
            good_list = good_list.next
        if carry:
            l3.next = ListNode(1)
        return l3copy.next
