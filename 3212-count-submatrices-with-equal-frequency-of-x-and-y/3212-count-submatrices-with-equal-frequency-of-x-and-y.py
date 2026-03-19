class Solution:
    def numberOfSubmatrices(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        cnt = 0

        prefix_sum_x = [[0] * (cols+1) for _ in range(rows+1)]
        prefix_sum_y = [[0] * (cols+1) for _ in range(rows+1)]
        

        for r in range(1, rows+1):
            for c in range(1, cols+1):
                val_x = 1 if grid[r-1][c-1] == 'X' else 0
                val_y = 1 if grid[r-1][c-1] == 'Y' else 0

                prefix_sum_x[r][c] = prefix_sum_x[r-1][c] + prefix_sum_x[r][c-1] - prefix_sum_x[r-1][c-1] + val_x
                prefix_sum_y[r][c] = prefix_sum_y[r-1][c] + prefix_sum_y[r][c-1] - prefix_sum_y[r-1][c-1] + val_y

                if prefix_sum_x[r][c] == prefix_sum_y[r][c] and prefix_sum_x[r][c] > 0:
                    cnt += 1
        return cnt
                