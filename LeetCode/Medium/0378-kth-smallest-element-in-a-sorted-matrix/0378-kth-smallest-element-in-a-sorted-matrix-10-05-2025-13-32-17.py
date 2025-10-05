from heapq import *

#convert lists to matrix
class Solution:
    def kthSmallest(self, lists, k):
        counter = 0
        min_heap = []
        output_list = []

        for idx in range(len(lists)):
            tmp = lists[idx].pop(0)
            heappush(min_heap, (tmp, idx))

        while min_heap:
            tmp = heappop(min_heap)
            counter += 1
            output_list.append(tmp[0])
            if counter == k:
                #print(output_list)
                return tmp[0]
            if lists[tmp[1]]:
                tmp2 = lists[tmp[1]].pop(0)
                heappush(min_heap, (tmp2, tmp[1]))
        return output_list[k - 1]
