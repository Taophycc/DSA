class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        island_sizes = {}
        island_id = 2
        max_island = 0
        directions = [(1, 0), (-1, 0), (0,1), (0, -1)]

        def dfs(r, c, current_id):
            grid[r][c] = current_id
            nonlocal current_size
            current_size += 1

            for dr, dc in directions:
                neigh_r, neigh_c = dr + r, dc + c

                if (0 <= neigh_r < rows) and (0 <= neigh_c < cols):
                    if grid[neigh_r][neigh_c] == 1:
                        dfs(neigh_r, neigh_c, current_id)


        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    current_size = 0
                    dfs(r, c, island_id)
                    island_sizes[island_id] = current_size
                    max_island = max(max_island, current_size)
                    island_id += 1

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    seen_islands = set()
                    potential_size = 1

                    for dr, dc in directions:
                        neigh_r, neigh_c = r + dr, c + dc

                        if 0 <= neigh_r < rows and 0 <= neigh_c < cols:
                            neighbor_val = grid[neigh_r][neigh_c]
                            if neighbor_val > 1:
                                seen_islands.add(neighbor_val)

                    for valid_id in seen_islands:
                        potential_size += island_sizes[valid_id]

                    max_island = max(max_island, potential_size)
        return max_island

                    


