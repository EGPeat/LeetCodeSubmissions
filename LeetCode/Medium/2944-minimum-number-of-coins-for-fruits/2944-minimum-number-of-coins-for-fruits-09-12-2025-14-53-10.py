class Solution:
    def minimumCoins(self, prices: List[int]) -> int:
        n = len(prices)
        queue = deque()
        queue.append(n)
        prices.append(0)
        for i in range(n - 1, -1, -1):
            maxCoveredIndex  = min(n, 2 * i + 2)
            while queue and queue[0] > maxCoveredIndex: #or >=
                queue.popleft()
            prices[i] += prices[queue[0]]
            while queue and prices[i] < prices[queue[-1]]:
                queue.pop()
            queue.append(i)
        return prices[0]