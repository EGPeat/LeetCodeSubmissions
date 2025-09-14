class Solution:
    def removeNthFromEnd(self, head, n):
        dummy = ListNode(next=head)
        fast, slow = dummy, dummy
        fast_counter = 0
        while fast != None and fast.next != None:
            if fast.next:
                fast = fast.next
                fast_counter += 1
        for i in range(fast_counter - n):
            slow = slow.next
        slow.next = slow.next.next
        return dummy.next
