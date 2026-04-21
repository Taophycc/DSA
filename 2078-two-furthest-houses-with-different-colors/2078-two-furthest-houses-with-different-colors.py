class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        n = len(colors)
        l, r = 0, n - 1
        while  colors[0] == colors[r]:
            r -= 1
        while colors[n-1] == colors[l]:
            l += 1
        return max(r, (n-1) - l)

        # if first and last element are different colors then that is the max distance
        # if not try to get the max distance from colors[0] and colors[n-1] respectively
        # r = max distance from the colors[n-1] to that point (r)
        # l is the max distance from colors[0] to that point (l)