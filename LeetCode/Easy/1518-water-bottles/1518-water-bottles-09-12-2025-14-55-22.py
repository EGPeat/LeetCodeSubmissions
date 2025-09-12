class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        counter = 0
        empty, full = 0, numBottles
        while (empty+full) >= numExchange:
            counter += full
            empty = empty + full
            full = 0
            exchange = (empty // numExchange)
            empty -= (empty // numExchange) * numExchange
            full += exchange
        return counter + full