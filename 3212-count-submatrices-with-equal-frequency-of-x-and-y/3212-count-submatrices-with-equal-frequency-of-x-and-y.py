class Solution:
    def numberOfSubmatrices(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        cnt = 0

        prefix_x = [[0] * (cols+1) for _ in range(rows+1)]
        prefix_y = [[0] * (cols+1) for _ in range(rows+1)]

        for r in range(1,rows+1):
            for c in range(1, cols+1):
                char = grid[r-1][c-1]
                val_x = 1 if char == 'X' else 0
                val_y = 1 if char == 'Y' else 0

                prefix_x[r][c] = prefix_x[r-1][c] + prefix_x[r][c-1] - prefix_x[r-1][c-1] + val_x
                prefix_y[r][c] = prefix_y[r-1][c] + prefix_y[r][c-1] - prefix_y[r-1][c-1] + val_y

                if prefix_x[r][c] > 0 and prefix_x[r][c] == prefix_y[r][c]:
                    cnt += 1
        return cnt