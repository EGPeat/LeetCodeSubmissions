import heapq
class Solution:
    def findClosestElements(self, arr, K, X):
        result = []
        #print(result)
        for item in arr:
            #print(item, result, abs(item - X))
            if len(result) < K or abs(item - X) < -result[0][0] or (abs(item - X) <= -result[0][0] and item <= result[0][1]): #< or <=
                heapq.heappush(result, (-abs(item - X), item))
            if len(result) > K:
                heapq.heappop(result)
        #print(result)
        output = [temp[1] for temp in result]
        output.sort()
        return output
