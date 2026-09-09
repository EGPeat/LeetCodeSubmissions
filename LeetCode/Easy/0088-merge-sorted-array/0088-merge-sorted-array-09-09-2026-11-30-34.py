class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        spot1 = m - 1
        spot2 = n - 1
        spot3 = len(nums1) - 1
        while spot3>= 0:
            if spot2 >=0 and spot1 >=0 and nums2[spot2] >= nums1[spot1]:
                nums1[spot3] = nums2[spot2]
                spot2 -= 1
            elif spot2 >=0 and spot1 >=0 and nums2[spot2] < nums1[spot1]:
                nums1[spot3] = nums1[spot1]
                spot1 -= 1
            elif spot1 >=0 and spot2 < 0:
                nums1[spot3] = nums1[spot1]
                spot1 -= 1
            elif spot2 >=0 and spot1 < 0:
                nums1[spot3] = nums2[spot2]
                spot2 -= 1
            spot3 -= 1
        