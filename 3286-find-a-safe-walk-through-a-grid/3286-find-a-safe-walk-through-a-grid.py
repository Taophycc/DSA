class Solution:
    def findSafeWalk(self, grid: List[List[int]], health: int) -> bool:
        rows, cols = len(grid), len(grid[0])
        max_grid_health = [[-1 for i in range(cols)] for _ in range(rows)]

        if grid[0][0] == 1:
            health -= 1
        
        max_grid_health[0][0] = health

        queue = deque([(0, 0)])

        directions = [(1, 0), (-1, 0), (0,1),(0, -1)]
        while queue:
            r,c = queue.popleft()
            current_health = max_grid_health[r][c]

            if r == rows -1 and c == cols - 1:
                return current_health >= 1

            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                if 0<= nr < rows and 0 <= nc < cols:
                    new_health = current_health - grid[nr][nc]
                    if  new_health > 0 and max_grid_health[nr][nc] == -1:
                        max_grid_health[nr][nc] = new_health
                        # 0-1 bfs
                        if grid[nr][nc] == 0:
                            queue.appendleft((nr, nc))
                        else:
                            queue.append((nr, nc))
                        
        return max_grid_health[rows-1][cols-1] >= 1




