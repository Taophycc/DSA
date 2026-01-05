class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        min_val = float('inf')
        sum_val = 0
        neg_count = 0

        for i in range(n):
            for j in range(n):
                num = matrix[i][j]
                
                if num < 0:
                    neg_count += 1

                min_val = min(min_val, abs(num))
                sum_val += abs(num)    
                
        if neg_count % 2 == 0:
            return sum_val
        return sum_val - 2 * min_val