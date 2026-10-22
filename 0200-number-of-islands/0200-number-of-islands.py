class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        visited = set()
        islands = 0
        
        def dfs(r,c):
            visited.add((r,c))

            directions = [(1,0), (-1, 0), (0, 1), (0, -1)]

            for dr, dc in directions:
                nr, nc = dr+r, dc+c

                if 0 <= nr < rows and 0 <= nc < cols:
                    if (nr, nc) not in visited and grid[nr][nc] == "1":
                        visited.add((nr, nc))
                        dfs(nr, nc)
        
        for r in range(rows):
            for c in range(cols):
                if (r, c) not in visited and grid[r][c] == "1":
                    islands += 1
                    dfs(r,c)
        return islands
        