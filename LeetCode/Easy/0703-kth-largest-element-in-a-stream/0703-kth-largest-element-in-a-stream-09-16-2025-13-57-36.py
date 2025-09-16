import heapq 


class KthLargest:
    def __init__(self, k, nums):
        self.nums = nums
        self.k_val = k
        heapq.heapify(self.nums)
        while len(self.nums) > self.k_val:
            heapq.heappop(self.nums)

    def add(self, num):
        heapq.heappush(self.nums, num)
        while len(self.nums) > self.k_val:
            heapq.heappop(self.nums)
        return self.nums[0]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)