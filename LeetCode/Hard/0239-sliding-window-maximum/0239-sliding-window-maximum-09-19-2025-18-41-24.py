class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        output = []
        maxheap = []
        q = [(-v, i) for i, v in enumerate(nums[: k - 1])]
        heapify(q)
        for i in range(k):
            heappush(maxheap, [-nums[i], i])
            #print(i, nums[:i+1])
            #print(maxheap)
        for i in range(k, len(nums)):
                #print("nums[i-k], maxheap", nums[i-k], maxheap)
                output.append(-maxheap[0][0])
                while maxheap and maxheap[0][1] <= i - k:
                    heappop(maxheap)

                heappush(maxheap, [-nums[i], i])
                #print(i, nums[i-k:i+1])
        output.append(-maxheap[0][0])
        return output