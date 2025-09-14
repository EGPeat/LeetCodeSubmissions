class Solution:
    def search_helper(self, arr, low, high, key):
        while low <= high:
            middle = low + (high - low) // 2
            if arr[middle] == key:
                return middle
            elif arr[middle] < key:
                low = middle + 1
            elif arr[middle] > key:
                high = middle - 1
        return -1

    def search(self, arr, key):
        n = len(arr) - 1
        start, end = 0, n
        while start < end:
            mid = start + (end - start) // 2
            if arr[mid] > arr[mid + 1]:
                start = mid
                break
            if arr[mid] < arr[start]:
                end = mid
            else:
                start = mid + 1

        maximum_spot = start
        if key < arr[0]:
            return self.search_helper(arr, maximum_spot + 1, n, key)
        else:
            return self.search_helper(arr, 0, maximum_spot, key)
