class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS, COLS = len(matrix), len(matrix[0])

        l, r = 0, (ROWS * COLS) - 1
        while l <= r:
            mid = (l + r) // 2
            row, col = mid // COLS, mid % COLS

            if matrix[row][col] < target:
                l = mid + 1
            elif matrix[row][col] > target:
                r = mid - 1
            else:
                return True
        return False