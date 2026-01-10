class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        max_area = 0

        l , r = 0, n-1

        while l<r:
            width = r-l
            curr_height = min(height[l], height[r])
            curr_area = width * curr_height
            max_area = max(curr_area, max_area)

            if height[l] < height[r]:
                l+=1
            else:
                r-=1
        return max_area