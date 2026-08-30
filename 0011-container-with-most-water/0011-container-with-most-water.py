class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_water = 0
        l, r = 0, len(height) - 1

        while l < r:
            area = (r-l)* min(height[l], height[r])
            max_water = max(area, max_water)
            if height[l] < height[r]:
                l+=1
            else:
                r -= 1
        return max_water