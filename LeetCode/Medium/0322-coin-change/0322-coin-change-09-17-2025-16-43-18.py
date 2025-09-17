class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            print("here")
            return 0
        if amount < coins[0]:
            print("here2")
            return - 1
        n = len(coins)
        dp = [[inf] * (amount + 1) for _ in range(n + 1)]
        dp[0][0] = 0
        coins.sort()
        for coin_idx in range(1, n + 1):
            curr_coin = coins[coin_idx - 1]
            for curr_amount in range(amount + 1):
                dp[coin_idx][curr_amount] = dp[coin_idx - 1][curr_amount]
                if curr_amount >= curr_coin:
                    dp[coin_idx][curr_amount] = min(
                        dp[coin_idx][curr_amount],
                        dp[coin_idx][curr_amount - curr_coin] + 1
                    )
        return -1 if dp[n][amount] == float('inf') else dp[n][amount]