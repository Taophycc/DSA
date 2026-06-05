class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        rows, cols = len(grid), len(grid[0])
        visited = set()
        island = 0

        def dfs(r,c):
            visited.add((r,c))
            directions = [(1, 0), (-1, 0),  (0, 1), (0, -1)]

            for dr, dc in directions:
                neigh_r, neigh_c = r + dr, c+ dc
                if (0 <= neigh_r < rows) and (0 <= neigh_c < cols):
                    if grid[neigh_r][neigh_c] == "1" and (neigh_r, neigh_c) not in visited:
                        dfs(neigh_r, neigh_c)

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r,c )not in visited:
                    island += 1
                    dfs(r, c)
        return island


