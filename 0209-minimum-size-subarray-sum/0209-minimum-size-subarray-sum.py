class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        n = len(nums)
        ans = n + 1  # max
        s = 0
        left = 0
        for right, x in enumerate(nums):  # x=nums[right]
            s += x
            while s >= target:
                ans = min(ans, right - left + 1)  # right==left时，get 1
                s -= nums[left]  # drop left one
                left += 1
        return ans if ans <= n else 0

