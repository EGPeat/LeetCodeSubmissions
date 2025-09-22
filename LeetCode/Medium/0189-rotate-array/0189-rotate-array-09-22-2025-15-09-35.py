class Solution:
    def notrotate(self, head, rotations):
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

    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        for i in range(k):
            tmp = nums.pop()
            nums.insert(0, tmp)