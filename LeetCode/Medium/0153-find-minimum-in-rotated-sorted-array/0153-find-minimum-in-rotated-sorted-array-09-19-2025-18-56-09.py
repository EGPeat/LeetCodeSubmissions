class Solution:
    def findMin(self, arr: List[int]) -> int:
        left, right = 0, len(arr) - 1
        boundary_index = 0

        while left < right:
            mid = (left + right) // 2
            if arr[mid] > arr[mid+1]:
                boundary_index = mid + 1
                right = mid - 1
            else:
                left = mid + 1

        return arr[boundary_index]