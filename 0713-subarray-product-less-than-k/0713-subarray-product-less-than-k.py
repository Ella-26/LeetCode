class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k <= 1:
            return 0
        ans = 0  # ans =0(no result) OR ans>=2(prodcut less than k,not nums[i])
        prod = 1
        left = 0
        for right, x in enumerate(nums):  # x=nums[right]
            prod *= x
            while prod >= k:
                prod /= nums[left]
                left += 1
            ans += right - left + 1  # right==left时，get 1
        return ans

