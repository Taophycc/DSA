class Solution:
    def countSubmatrices(self, grid: List[List[int]], k: int) -> int:
        rows = len(grid)
        cols = len(grid[0])
        cnt = 0

        for r in range(rows):
            for c in range(1, cols):
                grid[r][c] += grid[r][c-1]

        for r in range(rows):
            for c in range(cols):
                if r > 0:
                    grid[r][c] += grid[r-1][c]
                if grid[r][c] <= k:
                    cnt += 1
                else:
                    break
        return cnt