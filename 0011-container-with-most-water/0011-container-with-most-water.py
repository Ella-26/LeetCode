class Solution:
    def maxArea(self, height: List[int]) -> int:
        ans = 0
        left = 0
        right = len(height) - 1
        while left < right:  # firstly ensure weight is largest
            area = (right - left) * min(height[left], height[right])
            ans = max(ans, area)
            if (
                height[left] < height[right]
            ):  # weight is same, shorter one limits height, discard
                left += 1
            else:
                right -= 1
        return ans

