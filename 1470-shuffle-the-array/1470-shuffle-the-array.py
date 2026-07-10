from typing import List
class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        newnums = [0] * (2 * n)      # ← 创建 2n 大小的列表
        for i in range(n):
            newnums[2 * i] = nums[i]       # 放 x
            newnums[2 * i + 1] = nums[n + i]  # 放 y
        return newnums