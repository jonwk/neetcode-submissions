class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left, right = 0, len(heights)-1
        maxArea = 0
        while left < right:
            area = min(height[left],height[right])*(right - left + 1)
            if area > maxArea:
                maxArea = area
            elif height[left] > height[right]:
                right -= 1
            else:
                left += 1

        return maxArea


        