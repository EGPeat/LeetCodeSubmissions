class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        start = 0
        end = len(nums)-1
        output = self.findMajority_helper(nums, start, end)
        #print(f"final output is {output}")
        return output[0]
    
    def findMajority_helper(self, arr, start, end):
        if start == end:
                return (arr[start],1)
        middle = start + (end - start) // 2
        info_1 = self.findMajority_helper(arr, start, middle)
        info_2 = self.findMajority_helper(arr, middle+1, end)
        #print(info_1, info_2)
        #print(arr, start, middle, middle+1, end)
        if info_1[0] == info_2[0]:
            info_3 = (info_1[0], info_1[1] + info_2[1])
            #print(f"Got to the annoying spot, info_1[0] {info_1[0]}, info_1[1] + info_2[1]:{info_1[1] + info_2[1]}")
            return info_3
        info_1_count = arr[start:end + 1].count(info_1[0])
        #print(f"info_1_count: info_1[0] {info_1[0]}, info_1[1] {info_1[1]}, arr[middle+1:].count(info_1[0]) {arr[middle+1:].count(info_1[0])}")
        info_2_count = arr[start:end + 1].count(info_2[0])
        #print(f"info_2_count: info_2[0] {info_2[0]}, info_2[1] {info_2[1]}, arr[0:middle].count(info_2[0]) {arr[0:middle].count(info_2[0])}")

        return (info_1[0], info_1_count) if info_1_count > info_2_count else (info_2[0], info_2_count)

        return 0