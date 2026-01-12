class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        total_time = 0
        for i in range(n-1):
            curr = points[i]
            next_pnt = points[i+1]

            dx = abs(next_pnt[0]-curr[0])
            dy = abs(next_pnt[1]-curr[1])
            total_time += max(dy, dx)
        return total_time