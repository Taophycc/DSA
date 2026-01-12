class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        """
        Calculates the minimum time to visit all points in the given order.
        
        Approach:
        The problem allows movement in 8 directions (vertical, horizontal, diagonal).
        Each move takes 1 second. The optimal way to move between two points
        (x1, y1) and (x2, y2) is to move diagonally as much as possible, 
        because a diagonal move reduces BOTH the horizontal and vertical distance 
        at the same time.
        
        The time taken is determined by the longer distance (Chebyshev Distance):
        - If dx > dy: We move diagonally 'dy' times, then horizontally for the rest.
        - If dy > dx: We move diagonally 'dx' times, then vertically for the rest.
        
        Therefore, the cost for each segment is simply: max(|x2-x1|, |y2-y1|).
        
        Complexity:
        - Time: O(N) - We iterate through the list of points once.
        - Space: O(1) - We only store the total_time integer.
        """
        n = len(points)
        total_time = 0
        for i in range(n-1):
            curr = points[i]
            next_pnt = points[i+1]

            # Calculate absolute differences in X and Y
            dx = abs(next_pnt[0]-curr[0])
            dy = abs(next_pnt[1]-curr[1])
            
            # The time is the maximum of the two differences because diagonal 
            # moves cover both dimensions simultaneously.
            total_time += max(dy, dx)
            
        return total_time
