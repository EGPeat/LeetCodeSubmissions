class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        print(arr)
        output = []
        dist = float('inf')
        for i in range(1, len(arr)):
            #print(arr[i], arr[i-1], arr[i] - arr[i-1], dist, arr[i] - arr[i-1] < dist, arr[i] - arr[i-1] == dist)
            if arr[i] - arr[i-1] < dist:
                dist = arr[i] - arr[i-1]
                output = [[arr[i-1], arr[i]]]
            elif arr[i] - arr[i-1] == dist:
                output.append([arr[i-1], arr[i]])
        return output