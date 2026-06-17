class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        cnt = 0

        directions = [(1, 0), (-1,0), (0,1), (0,-1)]
        def dfs(r, c):
            grid[r][c] = -1


            for dr, dc in directions:
                nrow, ncol = dr + r, dc + c

                if 0 <= nrow < rows and 0 <= ncol < cols and grid[nrow][ncol] == 1:
                    dfs(nrow, ncol)

        for c in range(cols):
            if grid[0][c] == 1:
                dfs(0, c)
            if grid[rows - 1][c] == 1:
                dfs(rows - 1, c)
        
        for r in range(1, rows):
            if grid[r][0] == 1:
                dfs(r, 0)
            if grid[r][cols - 1] == 1:
                dfs(r, cols - 1)

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    cnt += 1

        return cnt