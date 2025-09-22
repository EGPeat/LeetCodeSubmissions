class Solution:
    def threeSumClosest(self, arr: List[int], target_sum: int) -> int:
        best_val = float('inf')
        n = len(arr)
        arr.sort()
        for i in range(n):
            if i > 0 and arr[i] == arr[i-1]:
                continue
            left = i+1
            right = n-1
            while(left < right):        
                added = arr[i] + arr[left] + arr[right]
                if added == target_sum:
                    return added

                if abs(added - target_sum) < abs(best_val - target_sum):
                    best_val = added
                if added > target_sum:
                    right -= 1
                else:
                    left += 1

        return best_val