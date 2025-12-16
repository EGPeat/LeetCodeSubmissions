class Solution:
    def threeSum(self, arr: List[int]) -> List[List[int]]:
        triplets = []
        arr.sort()
        for i in range(len(arr)-2):
            if i > 0 and arr[i] == arr[i-1]:
                continue
            left = i+1
            right = len(arr)-1
            while(left < right):        
                added = arr[i] + arr[left] + arr[right]
                if added == 0:
                    triplets.append([arr[i], arr[left], arr[right]])
                    left += 1
                    right -= 1
                    while left < right and arr[left] == arr[left - 1]:
                        left += 1
                    while left < right and arr[right] == arr[right + 1]:
                        right -= 1
                elif added > 0:
                    right -= 1
                else:
                    left += 1
                
        return triplets