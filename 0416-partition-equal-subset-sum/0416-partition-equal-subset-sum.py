class Solution:
    def canPartition(self, nums: list[int]) -> bool:
        s = sum(nums)
        # 分不了2set
        if s % 2:
            return False
        s //= 2

        f = [1] + [0] * s  # f[0]=1,others are 0
        for i, x in enumerate(nums):
            for j in range(s, x - 1, -1):
                # No x：直接f[j] Use x:凑j-x
                f[j] = f[j] or f[j - x]
            if f[s]:
                return True
        return False

