# Definition for singly-linked list.
#class ListNode:
#    def __init__(self, val=0, next=None):
#        self.val = val
#        self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head = None
        most_recent = None

        if not list1 and not list2:
            return
        elif list1 and not list2:
            return list1
        elif list2 and not list1:
            return list2

        while list1 or list2:
            if not list1:
                most_recent.next = list2
                return head
            elif not list2:
                most_recent.next = list1
                return head

            if list1.val <= list2.val:
                if not head:
                    head = list1
                else:
                    most_recent.next = list1
                most_recent = list1
                list1 = list1.next
            else:
                if not head:
                    head = list2
                else:
                    most_recent.next = list2
                most_recent = list2
                list2 = list2.next
        return head
