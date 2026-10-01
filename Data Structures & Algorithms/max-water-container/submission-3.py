class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1
        max_volume = (right - left) * min(heights[left], heights[right])

        while left < right:
            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1

            volume = (right - left) * min(heights[left], heights[right])
            max_volume = max(max_volume, volume)

        return max_volume
