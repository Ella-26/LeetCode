class Solution:
    def findPeakElement(self, nums: list[int]) -> int:
        # return any of the peaks
        # 只判断上下坡，如果上坡说明peak在right，下坡说明peak在左，另一半直接drop
        # [0,n-2] 判断mid和mid大小所以mid最大取n-2
        left = 0
        right = len(nums) - 2
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] > nums[mid + 1]:
                right = mid - 1
            else:
                left = mid + 1
        return left

