class Solution:
    def countSubmatrices(self, grid: List[List[int]], k: int) -> int:
        rows = len(grid)
        cols = len(grid[0])
        cnt = 0
        # padding the prefix array to create a buffer for the ground state or first row
        prefix_sum = [[0] * (cols + 1) for _ in range(rows + 1)]

        for r in range(1, rows+1):
            for c in range(1, cols+1):
                # inclusion-exclusion principle: above + left - diagonal + current_value
                prefix_sum[r][c] = prefix_sum[r-1][c] + prefix_sum[r][c-1] - prefix_sum[r-1][c-1] + grid[r-1][c-1]

                if prefix_sum[r][c] <= k:
                    cnt += 1
            
        return cnt