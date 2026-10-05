class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        n = len(coins)

        f = [inf] * (amount + 1)
        f[0] = 0

        for x in coins:
            for c in range(x, amount + 1):
                f[c] = min(f[c], f[c - x] + 1)
        ans = f[amount]
        return ans if ans < inf else -1

