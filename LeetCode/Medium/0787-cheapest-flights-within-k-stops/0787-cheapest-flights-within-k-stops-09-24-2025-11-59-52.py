class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        INF = 0x3F3F3F3F
        dist = [INF] * n
        dist[src] = 0
        for _ in range(k + 1):
            backup = dist.copy()
            for from_city, to_city, price in flights:
                dist[to_city] = min(dist[to_city], backup[from_city] + price) 
        return -1 if dist[dst] == INF else dist[dst]
