class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        n = len(nums)
        ans = []
        path = []

        def dfs(i):
            # 边界条件：i 到什么时候，就没有元素可以决策了
            if i == n:
                # path.pop() 会直接修改path，如果没有copy而是直接path的话
                ans.append(path.copy())
                return

            # 决策 A（不选 nums[i]）
            dfs(i + 1)
            # 决策 B（选 nums[i]）
            # 不管选还是不选，后面 nums[i+1..n-1] 都还没决定
            # 所以两条路都要 dfs(i+1) 去处理后面
            # 唯一区别：选 → 把 nums[i] 先塞进 path；不选 → path 不动
            path.append(nums[i])
            dfs(i + 1)
            path.pop()

        dfs(0)
        return ans

