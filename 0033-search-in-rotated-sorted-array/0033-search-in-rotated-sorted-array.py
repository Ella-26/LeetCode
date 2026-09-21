class Solution:
    def search(self, nums: list[int], target: int) -> int:
        # 只判断mid什么时候为蓝
        def is_blue(i: int) -> bool:
            end = nums[-1]
            if (
                nums[i] > end
            ):  # mid在第一段，为蓝需要同时满足target同段且在mid前（仅这种情况）
                return target > end and nums[i] >= target
            else:  # 第二段，同段target在mid之前或者target在第一段都可
                return target > end or nums[i] >= target

        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2
            if is_blue(mid):
                right = mid - 1
            else:
                left = mid + 1
        # 结束后left=第一个出现蓝色的位置，这时候不！=targe说明没结果，全蓝or全红都没结果
        if left == len(nums) or nums[left] != target:
            return -1
        return left

