class Solution:
    def minPathSum(self, grid: list[list[int]]) -> int:
        m, n = len(grid), len(grid[0])
        # m+1行，n+1列，初始化为inf，这样找到小的就更新，大一圈是防止左上角没有左边上边不好处理
        f = [[inf] * (n + 1) for _ in range(m + 1)]
        f[0][1] = 0
        for i, row in enumerate(grid):
            for j, x in enumerate(row):
                # 到当前位置只能从左边或者上面过来
                f[i + 1][j + 1] = min(f[i + 1][j], f[i][j + 1]) + x
        return f[m][n]

