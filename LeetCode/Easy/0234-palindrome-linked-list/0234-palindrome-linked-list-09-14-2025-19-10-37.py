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

    def isPalindrome(self, head):
        fast = head
        slow = head

        while fast is not None and fast.next:
            fast = fast.next.next
            slow = slow.next
        slow2 = head
        middle = slow

        head_second_half = self.reverse(slow)  # reverse the second half
        copy_head_second_half = head_second_half

        while (slow2 is not None and head_second_half is not None):
            if head_second_half.val != slow2.val:
                #print_list(head)
                return False
            head_second_half = head_second_half.next
            slow2 = slow2.next
        #print_list(head)
        self.reverse(copy_head_second_half)
        
        return True

def print_list(head):
    print(f"{head.val}", end=" ")
    while head.next:
        head = head.next
        print(f"-> {head.val}", end=" ")
        