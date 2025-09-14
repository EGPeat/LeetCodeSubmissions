
class Solution:
    def nextGreatestLetter(self, arr, key):
        n = len(arr)
        if key >= arr[n - 1]:  # if the 'key' is bigger than the biggest element
            return arr[0]

        start, end = 0, n - 1
        while start <= end:
            mid = start + (end - start) // 2
            if key < arr[mid]:
                end = mid - 1
            elif key >= arr[mid]:
                start = mid + 1
            else:
                return arr[mid]
        return arr[start]
