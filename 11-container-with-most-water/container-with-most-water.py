class Solution:
    def maxArea(self, height: List[int]) -> int:
        areas = []
        left, right = 0, len(height) - 1

        while left < right:
            if height[left] < height[right]:
                areas.append(height[left] * (right - left))
                left += 1
            elif height[left] > height[right]:
                areas.append(height[right] * (right - left))
                right -= 1
            else:
                areas.append(height[right] * (right - left))
                left += 1
                right -= 1

        return max(areas)
