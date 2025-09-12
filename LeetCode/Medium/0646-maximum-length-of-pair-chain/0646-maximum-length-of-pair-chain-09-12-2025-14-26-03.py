class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs.sort(key=lambda x: x[1])
        chain = [pairs[0]]
        for link in pairs:
            if link[0] > chain[-1][1]:
                chain.append(link)
        return len(chain)