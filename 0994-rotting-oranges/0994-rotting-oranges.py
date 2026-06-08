class Solution:
    from collections import deque
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        queue = deque()
        freshOranges = 0
        minutes = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    queue.append((r,c))
                elif grid[r][c] == 1:
                    freshOranges += 1

        if freshOranges == 0:
            return 0

        directions = [(1, 0), (-1,0), (0,1), (0,-1)]
        while queue and freshOranges > 0:
            minutes += 1

            for _ in range(len(queue)):
                r, c = queue.popleft()
            
                for dr, dc in directions:
                    neigh_r, neigh_c = dr + r, dc + c

                    if (0 <= neigh_r < rows) and (0 <= neigh_c < cols) and grid[neigh_r][neigh_c] == 1 :
                        grid[neigh_r][neigh_c] = 2
                        freshOranges -=1
                        queue.append((neigh_r, neigh_c))

        return minutes if freshOranges == 0 else -1