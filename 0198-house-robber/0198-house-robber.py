class Solution:
    def rob(self, nums: list[int]) -> int:
        n = len(nums)
        cache = [-1] * n  # save dfs(i)
        ans = -1

        # 思路：0～i间房子，最多能偷多少？select or not
        def dfs(i):
            if i < 0:  # 0~-1 house illegal
                return 0
            if cache[i] != -1:  # already save dfs(i) in cache
                return cache[i]
            res = max(dfs(i - 1), dfs(i - 2) + nums[i])
            cache[i] = res
            return res

        ans = dfs(n - 1)
        return ans

