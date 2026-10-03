class Solution:
    def combinationSum3(self, k: int, n: int) -> list[list[int]]:
        ans = []
        path = []

        def dfs(i, t):
            d = k - len(path)  # How many left to count to k
            # t:还差多少到n
            # t减到超过n了错误，或者t>剩下的数的可能最大和，怎么都选不够到n了
            if t < 0 or t > (i * 2 - d + 1) * d // 2:
                return

            if len(path) == k:  # That's enough k, save ans
                ans.append(path.copy())
                return

            for j in range(
                i, d - 1, -1
            ):  # interate backwards,Guarantee that the remaining number is enough, so only to d-1
                path.append(j)
                dfs(j - 1, t - j)  # chose j, so t-j
                path.pop()

        dfs(9, n)
        return ans

