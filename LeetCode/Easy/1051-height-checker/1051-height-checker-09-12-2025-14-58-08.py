class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        maxElement = max(heights, default=0)
        count = [0] * (maxElement + 1)

        for element in heights:
            count[element] += 1
        result = []
        counter = 0
        currheight = 0
        for idx in range(len(heights)):
            while count[currheight] == 0:
                currheight += 1
            if heights[idx] != currheight:
                counter += 1
                
            count[currheight] -= 1

        return counter