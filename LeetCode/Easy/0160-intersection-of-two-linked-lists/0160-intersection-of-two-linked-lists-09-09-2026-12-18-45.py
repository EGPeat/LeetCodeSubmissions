# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        set_nodes= set()
        while headA:
            set_nodes.add(headA)
            headA = headA.next
        while headB:
            if headB in set_nodes:
                return headB
            set_nodes.add(headB)
            headB = headB.next
        
        else:
            return None