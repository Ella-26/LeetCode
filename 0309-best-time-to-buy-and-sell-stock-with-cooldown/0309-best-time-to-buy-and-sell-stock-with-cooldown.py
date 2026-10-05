class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        # f[i][0] = 第 i 天结束后，不持有股票时的最大利润
        # f[i][1] = 第 i 天结束后，持有股票时的最大利润
        n = len(prices)
        f = [[0] * 2 for _ in range(n + 1)]

        # 没开始之前
        f[0][0] = 0
        f[0][1] = float("-inf")

        for i in range(n):
            p = prices[i]

            # 第 i+1 天结束时，不持有
            f[i + 1][0] = max(f[i][0], f[i][1] + p)  # 今天什么都不做  # 今天卖出

            # 第 i+1 天结束时，持有
            f[i + 1][1] = max(f[i][1], f[i - 1][0] - p)  # 今天什么都不做  # 今天买入

        return f[n][0]

