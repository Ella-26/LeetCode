class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        pairs = sorted((v, i) for i, v in enumerate(nums))
        ans = []
        n = len(nums)
        left = 0
        right = n - 1
        while left < right:
            s = pairs[left][0] + pairs[right][0]
            if s == target:
                return [pairs[left][1], pairs[right][1]]
                break
            if s > target:
                right -= 1
            else:
                left += 1

        return []

