class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        if len(nums2) < len(nums1):
            nums2, nums1 = nums1, nums2
        for number1 in nums1:
            start, end = 0, len(nums2) - 1
            while start <= end:
                mid = start + (end - start) // 2
                if nums2[mid] == number1:
                    return number1
                if nums2[mid] < number1:
                    start = mid + 1
                else:
                    end = mid - 1



        return -1