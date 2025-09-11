# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    def __lt__(self, other):
        return self.val < other.val
    def __le__(self, other):
        return self.val <= other.val
    def __gt__(self, other):
       return self.val > other.val
    def __eq__(self, other):
        if self.val == other.val:
            return True
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        from heapq import heappop, heappush, heapify
        counter = 0
        heap = []
        for i, lst in enumerate(lists):
            if lst:
                counter += 1
                heappush(heap, (lst.val, counter, lst))

        dummy = ListNode(0)
        curr = dummy
        while heap:
            num, _, node = heappop(heap)
            number = node.val
            curr.next = node
            curr = node
            if node.next:
                counter += 1
                heappush(heap, (node.next.val, counter, node.next))
        return dummy.next