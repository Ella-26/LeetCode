class Solution:
    def combine(self, n: int, k: int) -> list[list[int]]:
        ans = []
        path = []

        def dfs(i):
            d = k - len(path)  # 还剩多少个数到k
            if i < d:  # 没得选了永远不可能到k
                return

            if len(path) == k:  # 够k个了，存ans，不用判断因为不可能重复
                ans.append(path.copy())
                return

            for j in range(i, 0, -1):  # interate backwards
                path.append(j)
                dfs(j - 1)
                path.pop()

        dfs(n)
        return ans

