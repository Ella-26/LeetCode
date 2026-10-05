class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        f = [1] * n
        # j:在i前面找，看谁能接到当前数后面
        # f[i]:必须以nums[i]结尾，最长多长
        for i in range(n):
            for j in range(i):
                if nums[j] < nums[i]:
                    f[i] = max(f[i], f[j] + 1)

        return max(f)

