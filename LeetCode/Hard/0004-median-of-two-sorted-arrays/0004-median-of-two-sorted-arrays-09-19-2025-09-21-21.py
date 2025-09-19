class Solution:
    def find_kth_element(self, nums1, nums2, index1: int, index2: int, k: int) -> int:
            len_nums1 = len(nums1)
            len_nums2 = len(nums2)
            if index1 >= len_nums1:
                return nums2[index2 + k - 1]          
            if index2 >= len_nums2:
                return nums1[index1 + k - 1]
            if k == 1:
                return min(nums1[index1], nums2[index2])
          
            half_k = k // 2
          
            nums1_mid_value = nums1[index1 + half_k - 1] if index1 + half_k - 1 < len_nums1 else float('inf')
            nums2_mid_value = nums2[index2 + half_k - 1] if index2 + half_k - 1 < len_nums2 else float('inf')
          
            if nums1_mid_value < nums2_mid_value:
                return self.find_kth_element(nums1, nums2, index1 + half_k, index2, k - half_k)
            else:
                return self.find_kth_element(nums1, nums2, index1, index2 + half_k, k - half_k)
      
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        len_nums1, len_nums2 = len(nums1), len(nums2)
        total_length = len_nums1 + len_nums2
        left_median = self.find_kth_element(nums1, nums2, 0, 0, (total_length + 1) // 2)
        right_median = self.find_kth_element(nums1, nums2, 0, 0, (total_length + 2) // 2)
        return (left_median + right_median) / 2.0