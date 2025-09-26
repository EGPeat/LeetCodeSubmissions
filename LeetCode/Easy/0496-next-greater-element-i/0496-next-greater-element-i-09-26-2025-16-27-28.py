class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums_dict = {}
        n = len(nums2)
        for i, num in enumerate(nums2):
            if num not in nums_dict:
                nums_dict[num] = i
        #print(nums_dict)
        output = []
        for item in nums1:
            output.append(-1)
            if max(nums_dict.keys()) > item:
                #print(nums_dict[item])
                for idx in range(nums_dict[item], n):
                    #print(item, nums2[idx], idx)
                    if nums2[idx] > item:
                        output.pop()
                        output.append(nums2[idx])
                        break
        return output