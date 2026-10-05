MX = 10000
f = [0] + [inf] * MX
for i in range(1, isqrt(MX) + 1):
    for j in range(i * i, MX + 1):
        # 不用当前:f[j] 用当前:凑
        f[j] = min(f[j], f[j - i * i] + 1)  # 不选 vs 选


class Solution:
    def numSquares(self, n: int) -> int:
        return f[n]

