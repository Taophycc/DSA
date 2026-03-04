class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        nums_row = len(mat)
        nums_col = len(mat[0])

        row_count = [0] * nums_row
        col_count = [0] * nums_col

        for r in range(nums_row):
            for c in range(nums_col):
                val = mat[r][c]
                row_count[r] += val
                col_count[c] += val

        special_count = 0
        
        for r in range(nums_row):
            for c in range(nums_col):
                if mat[r][c] == 1 and row_count[r] == 1 and col_count[c] == 1:
                    special_count += 1
                    
        return special_count