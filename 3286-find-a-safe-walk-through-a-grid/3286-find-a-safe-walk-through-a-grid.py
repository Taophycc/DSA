class Solution:
    def findSafeWalk(self, grid: List[List[int]], health: int) -> bool:
        rows, cols = len(grid), len(grid[0])
        max_health_grid = [[-1 for i in range(cols)] for _ in range(rows)]

        if grid[0][0] == 1:
            health -= 1
        
        max_health_grid[0][0] = health

        queue = deque([(0, 0, health)])

        directions = [(1, 0), (-1, 0), (0,1),(0, -1)]
        while queue:
            r,c,h = queue.popleft()

            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                if 0<= nr < rows and 0 <= nc < cols:
                    new_health = h - grid[nr][nc]
                    if  new_health > 0 and new_health > max_health_grid[nr][nc]:
                        max_health_grid[nr][nc] = new_health
                        queue.append((nr, nc, new_health))
        return True if max_health_grid[rows-1][cols-1] >= 1 else False




