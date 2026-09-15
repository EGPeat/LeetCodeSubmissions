class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        set1 = set(nums1)
        set2 = set()
        output = []
        for num in nums2:
            if num in set1 and num not in set2:
                output.append(num)
                set2.add(num)
        return output