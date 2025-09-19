# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        node_dict = defaultdict(list)
        dummy = ListNode(next = head)
        while head:
            node_dict[head.val].append(head)
            head = head.next
        #print(node_dict.keys())
        keys_list = list(node_dict.keys())
        keys_list.sort()
        #print(keys_list)
        #dummy.next = node_dict[keys_list[0]]
        prev = dummy
        for i in range(len(keys_list)):
            curr = node_dict[keys_list[i]]
            #print(curr, len(curr))
            if len(curr) > 1:
                for item in curr:
                    prev.next = item
                    prev = item
            else:
                curr = curr[0]

                prev.next = curr
                prev = curr
        prev.next = None
        return dummy.next