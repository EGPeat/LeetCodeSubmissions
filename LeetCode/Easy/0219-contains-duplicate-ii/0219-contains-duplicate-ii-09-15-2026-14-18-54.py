class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        num_dict = {}
        order_list = []
        for idx, number in enumerate(nums):
            
            if len(order_list)>k:
                num_loc = order_list.pop(0)
                del num_dict[num_loc]
            if num_dict.get(number, -1) != -1:
                return True
            else:
                num_dict[number] = idx
                order_list.append(number)
        return False

