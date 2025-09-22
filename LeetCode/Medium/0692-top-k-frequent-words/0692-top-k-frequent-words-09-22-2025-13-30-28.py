class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        counted = Counter(words)
        counted_setup = [(-y,x) for x,y in counted.items()]
        heapq.heapify(counted_setup)
        idx = 0
        output = []
        while counted_setup and idx < k:
            tmp = heapq.heappop(counted_setup)
            output.append(tmp[1])
            idx+=1
        return output